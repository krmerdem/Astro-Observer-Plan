# -*- coding: utf-8 -*-
"""observatories.py veri butunlugu testleri."""

import re
import sys
from collections import Counter
from pathlib import Path

import pytest

try:
    from zoneinfo import available_timezones
except ImportError:  # Python < 3.9
    available_timezones = None

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observatories import observatories  # noqa: E402

REQUIRED_KEYS = {"latitude", "longitude", "elevation", "timezone"}
LAT_RE = re.compile(r'^\d+°\s*\d+\'\s*[\d.]+"\s*[NS]$')
LON_RE = re.compile(r'^\d+°\s*\d+\'\s*[\d.]+"\s*[EW]$')


def test_not_empty():
    assert len(observatories) > 100


def test_no_silently_dropped_duplicate_keys():
    """Dict literali yinelenen anahtari sessizce dusurur; kaynakta dup olmamali."""
    src = (Path(__file__).resolve().parents[1] / "observatories.py").read_text(
        encoding="utf-8"
    )
    keys = re.findall(r'\n\s{4}"([^"]+)":\s*\{', src)
    dups = [k for k, c in Counter(keys).items() if c > 1]
    assert not dups, "Yinelenen gozlemevi anahtarlari: {}".format(dups)
    assert len(keys) == len(observatories)


@pytest.mark.parametrize("name", list(observatories))
def test_required_keys_present(name):
    assert REQUIRED_KEYS <= set(observatories[name]), name


@pytest.mark.parametrize("name", list(observatories))
def test_elevation_is_numeric(name):
    float(observatories[name]["elevation"])  # ValueError ise test patlar


@pytest.mark.parametrize("name", list(observatories))
def test_coordinate_format(name):
    data = observatories[name]
    assert LAT_RE.match(data["latitude"]), (name, data["latitude"])
    assert LON_RE.match(data["longitude"]), (name, data["longitude"])


@pytest.mark.skipif(available_timezones is None, reason="zoneinfo yok")
@pytest.mark.parametrize("name", list(observatories))
def test_timezone_is_valid(name):
    assert observatories[name]["timezone"] in available_timezones(), name
