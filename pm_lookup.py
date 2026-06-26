# -*- coding: utf-8 -*-
"""Pecaut & Mamajek (2013) EEM_dwarf_UBVIJHK_colors_Teff lookup helpers.

Ana sequence (V) yildizlari icin, secilen bir renk indeksi degerine en yakin
tablo satirlarini bulan bagimsiz ve test edilebilir yardimci fonksiyonlar.

Kaynak tablo: pecaut_mamajek.py (liste-of-dict).
Referans: https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt

Not: Bu modul yalniz veriye baglidir, herhangi bir GUI bagimliligi yoktur;
bu sayede ana uygulama tarafindan import edilebilir ve ayrica test edilebilir.
"""

from pecaut_mamajek import pecaut_mamajek as _TABLE

# Tabloda eksik deger icin kullanilan isaretler ('...', '....', '.....').
# Hepsi yalnizca noktadan olusur.

# Tabloda gercekten bulunan renk indeksi sutunlari.
COLOR_INDICES = (
    "B-V", "Bt-Vt", "G-V", "Bp-Rp", "G-Rp", "b-y", "U-B",
    "V-Rc", "V-Ic", "V-Ks", "J-H", "H-Ks", "Ks-W1",
    "W1-W2", "W1-W3", "W1-W4", "g-r", "i-z", "z-Y",
)

# Kullanici dostu kisaltma -> tablodaki gercek sutun adi.
ALIASES = {
    "H-K": "H-Ks",
    "V-K": "V-Ks",
    "V-R": "V-Rc",
    "V-I": "V-Ic",
}


def _to_float(raw):
    """Tablo hucresini float'a cevirir; eksik/gecersiz deger icin None doner."""
    if raw is None:
        return None
    s = str(raw).strip()
    if not s or set(s) <= {"."}:  # '', '...', '.....' gibi eksik isaretleri
        return None
    try:
        return float(s)
    except ValueError:
        return None


def resolve_column(name):
    """Verilen renk indeksi adini tablodaki gercek sutun adina cozumler."""
    if name in _TABLE[0]:
        return name
    if name in ALIASES:
        return ALIASES[name]
    raise KeyError(
        "Bilinmeyen renk indeksi: {!r}. Gecerli olanlar: {}".format(
            name, ", ".join(COLOR_INDICES)
        )
    )


def available_indices():
    """Tabloda en az bir gecerli degeri bulunan renk indekslerini listeler."""
    result = []
    for col in COLOR_INDICES:
        if any(_to_float(row.get(col)) is not None for row in _TABLE):
            result.append(col)
    return result


def nearest(color, value, n=2):
    """`color` indeksinde `value` degerine en yakin `n` satiri doner.

    Donen liste yakinliga gore siralidir (en yakin once). O sutunda eksik
    degeri olan satirlar gozardi edilir.
    """
    col = resolve_column(color)
    value = float(value)
    candidates = []
    for row in _TABLE:
        fv = _to_float(row.get(col))
        if fv is not None:
            candidates.append((abs(fv - value), fv, row))
    candidates.sort(key=lambda t: t[0])
    return [row for _, _, row in candidates[:n]]


def bracketing(color, value):
    """`value`'yu alttan ve ustten saran iki satiri (alt, ust) olarak doner.

    Deger tablonun disindaysa ilgili tarafta None doner. Tam esitlikte ayni
    satir hem alt hem ust olabilir. Enterpolasyon icin uygundur.
    """
    col = resolve_column(color)
    value = float(value)
    pairs = [
        (_to_float(row.get(col)), row)
        for row in _TABLE
        if _to_float(row.get(col)) is not None
    ]
    lower = max((p for p in pairs if p[0] <= value), key=lambda p: p[0], default=None)
    upper = min((p for p in pairs if p[0] >= value), key=lambda p: p[0], default=None)
    return (lower[1] if lower else None, upper[1] if upper else None)


def interpolate(color, value, target):
    """`color` = `value` icin `target` parametresini dogrusal enterpole eder.

    Ornek: interpolate("B-V", 0.65, "Teff") -> ~5770.
    Saran satirlardan birinde target eksikse en yakin satirin degeri doner.
    Hicbir gecerli deger yoksa None doner.
    """
    lower, upper = bracketing(color, value)
    col = resolve_column(color)

    def tv(row):
        return _to_float(row.get(target)) if row else None

    lo_x, hi_x = (_to_float(lower.get(col)) if lower else None,
                  _to_float(upper.get(col)) if upper else None)
    lo_y, hi_y = tv(lower), tv(upper)

    if lo_y is not None and hi_y is not None and lo_x is not None and hi_x is not None:
        if hi_x == lo_x:
            return lo_y
        frac = (value - lo_x) / (hi_x - lo_x)
        return lo_y + frac * (hi_y - lo_y)
    # Saranlardan biri eksikse mevcut olani dondur.
    if lo_y is not None:
        return lo_y
    if hi_y is not None:
        return hi_y
    # Son care: en yakin gecerli target.
    for row in nearest(color, value, n=len(_TABLE)):
        y = tv(row)
        if y is not None:
            return y
    return None


def row_params(row):
    """Satirdaki tum alanlari sayisal (float) ya da None olarak ayristirir.

    SpT gibi metin alanlar oldugu gibi birakilir.
    """
    out = {}
    for key, val in row.items():
        if key in ("#SpT", "#SpT.1"):
            out[key] = val
        else:
            out[key] = _to_float(val)
    return out


if __name__ == "__main__":
    # Hizli demo: Gunes-benzeri bir yildiz (B-V ~ 0.65)
    print("Mevcut renk indeksleri:", ", ".join(available_indices()))
    rows = nearest("B-V", 0.65, n=2)
    print("\nB-V=0.65 icin en yakin 2 satir:")
    for r in rows:
        print("  {SpT:>6}  B-V={bv}  Teff={teff}".format(
            SpT=r["#SpT"], bv=r["B-V"], teff=r["Teff"]))
    print("\nB-V=0.65 -> enterpole Teff:", round(interpolate("B-V", 0.65, "Teff"), 1))
