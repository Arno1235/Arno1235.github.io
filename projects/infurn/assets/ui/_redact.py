#!/usr/bin/env python3
"""Crop real app screenshots to identical window bounds for the portfolio."""
from pathlib import Path
from PIL import Image
import numpy as np

SRC = Path('design/screenshots')
OUT = Path('docs/assets/ui')

SPECS = [
    ('1_prepare.png', 'prepare.jpg'),
    ('2_library.png', 'library.jpg'),
    ('3_jobs.png', 'jobs.jpg'),
    ('4_resulst_wipe.png', 'results.jpg'),
    ('4_results_grid.png', 'results-grid.jpg'),
]

def window_box(im):
    arr = np.asarray(im.convert('RGB'))
    corner = arr[5:25, 5:25].mean(axis=(0, 1))
    diff = np.abs(arr.astype(np.float32) - corner).mean(axis=2)
    mask = diff > 18
    ys, xs = np.where(mask)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    crops = []
    for src_name, out_name in SPECS:
        im = Image.open(SRC / src_name).convert('RGB')
        crops.append((out_name, im.crop(window_box(im))))
    sizes = {c.size for _, c in crops}
    assert len(sizes) == 1, sizes
    for out_name, crop in crops:
        crop.save(OUT / out_name, quality=90, optimize=True)
        print('wrote', out_name, crop.size)

if __name__ == '__main__':
    main()
