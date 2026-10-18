"""Obrazy wariantów stoiska w hero (Economy / Smart / Premium).

Użycie:
    python tools/warianty.py ŚCIEŻKA_DO_FOLDERU_Z_PNG

W folderze mogą być dowolne z plików (PNG lub JPG, najlepiej 2560×1440 lub 1920×1080, 16:9):
    stoisko-economy.png   stoisko-smart.png   stoisko-premium.png
Każdy znaleziony plik zamienia się na:
    assets/img/warianty/stoisko-<wariant>-<640|960|1280|1920>.avif / .webp

Nazwy plików na stronie są stałe, więc nie trzeba przebudowywać HTML — wystarczy
wgrać nowe pliki (commit + push). Ważne: wszystkie trzy obrazy z tej samej kamery
(CAM_EXPO_MAIN) i w tym samym kadrze, bo punkty z opisami mają stałe położenie.
Wymaga: pip install pillow  (Pillow ≥ 11.2 ma wbudowany zapis AVIF).
"""
import os
import sys

from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(ROOT, "assets", "img", "warianty")
WIDTHS = [640, 960, 1280, 1920]
VARIANTS = ["economy", "smart", "premium"]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    os.makedirs(DST, exist_ok=True)
    done = 0
    for v in VARIANTS:
        path = next((os.path.join(src, f"stoisko-{v}.{e}") for e in ("png", "jpg", "jpeg", "webp")
                     if os.path.exists(os.path.join(src, f"stoisko-{v}.{e}"))), None)
        if not path:
            print("pominięto (brak pliku):", v)
            continue
        im = Image.open(path).convert("RGB")
        w0, h0 = im.size
        if abs(w0 / h0 - 16 / 9) > 0.01:  # przytnij do 16:9 od środka
            nh = round(w0 * 9 / 16)
            top = max(0, (h0 - nh) // 2)
            im = im.crop((0, top, w0, top + nh))
        for w in WIDTHS:
            r = im.resize((w, round(w * 9 / 16)), Image.LANCZOS)
            r = r.filter(ImageFilter.UnsharpMask(radius=0.6, percent=40, threshold=2))
            r.save(os.path.join(DST, f"stoisko-{v}-{w}.webp"), "WEBP", quality=82, method=6)
            r.save(os.path.join(DST, f"stoisko-{v}-{w}.avif"), "AVIF", quality=58, speed=4)
        print("OK", v, im.size)
        done += 1
    print(f"Gotowe: {done} z 3. Pliki w assets/img/warianty/")


if __name__ == "__main__":
    main()
