# -*- coding: utf-8 -*-
"""pecaut_mamajek.py tablo butunlugu ve pm_lookup testleri."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pecaut_mamajek import pecaut_mamajek as TABLE  # noqa: E402
import pm_lookup  # noqa: E402


# --- Tablo butunlugu ---------------------------------------------------------

def test_table_not_empty():
    assert len(TABLE) > 100


def test_all_rows_share_same_columns():
    expected = set(TABLE[0])
    for row in TABLE:
        assert set(row) == expected, row.get("#SpT")


def test_spt_columns_consistent():
    for row in TABLE:
        assert row["#SpT"] == row["#SpT.1"], row["#SpT"]


def test_spt_values_unique():
    spts = [row["#SpT"] for row in TABLE]
    assert len(spts) == len(set(spts))


def test_teff_is_monotonic_decreasing():
    """Tablo O (sicak) -> Y (soguk) sirali; Teff azalan olmali."""
    teffs = [float(row["Teff"]) for row in TABLE]
    assert teffs == sorted(teffs, reverse=True)


# --- pm_lookup ---------------------------------------------------------------

def test_to_float_handles_missing_markers():
    for marker in ("...", "....", ".....", "", None):
        assert pm_lookup._to_float(marker) is None
    assert pm_lookup._to_float("0.65") == 0.65
    assert pm_lookup._to_float("-0.33") == -0.33


def test_resolve_column_alias():
    assert pm_lookup.resolve_column("H-K") == "H-Ks"
    assert pm_lookup.resolve_column("B-V") == "B-V"
    with pytest.raises(KeyError):
        pm_lookup.resolve_column("YOK-YOK")


def test_available_indices_nonempty():
    idx = pm_lookup.available_indices()
    assert "B-V" in idx and "J-H" in idx


def test_nearest_returns_sorted_by_distance():
    rows = pm_lookup.nearest("B-V", 0.65, n=3)
    assert len(rows) == 3
    dists = [abs(float(r["B-V"]) - 0.65) for r in rows]
    assert dists == sorted(dists)


def test_nearest_solar_bv_is_g_type():
    """B-V=0.65 Gunes degeridir; en yakin satir G tayfinda olmali."""
    nearest = pm_lookup.nearest("B-V", 0.65, n=1)[0]
    assert nearest["#SpT"].startswith("G")
    assert float(nearest["Teff"]) == pytest.approx(5770, abs=100)


def test_nearest_skips_missing_values():
    """Donen tum satirlarin ilgili sutunda gecerli degeri olmali."""
    for row in pm_lookup.nearest("i-z", 1.0, n=5):
        assert pm_lookup._to_float(row["i-z"]) is not None


def test_bracketing_orders_low_high():
    low, high = pm_lookup.bracketing("B-V", 0.65)
    assert float(low["B-V"]) <= 0.65 <= float(high["B-V"])


def test_interpolate_exact_value():
    # G2V satiri B-V=0.65, Teff=5770 -> tam esitlikte enterpolasyon birebir
    assert pm_lookup.interpolate("B-V", 0.65, "Teff") == pytest.approx(5770, abs=1)


def test_interpolate_between_rows_is_bounded():
    val = pm_lookup.interpolate("B-V", 0.655, "Teff")
    assert 5720 <= val <= 5770


def test_row_params_parses_numbers_keeps_spt():
    params = pm_lookup.row_params(TABLE[0])
    assert params["#SpT"] == TABLE[0]["#SpT"]
    assert isinstance(params["Teff"], float)
    # Eksik isaretli alanlar None olmali
    assert params["G-V"] is None
