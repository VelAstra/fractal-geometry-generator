"""
Preview Generator for Classical Fractals.
Renders high-resolution samples of Mandelbrot, Julia, and Barnsley Fern.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PIL import Image
from core.mandelbrot import compute_mandelbrot, compute_julia
from core.geometric_fractals import generate_barnsley_fern, generate_koch_snowflake
from core.color_maps import apply_colormap


def generate_all_previews(output_dir: str = "sample_data", size: int = 512):
    os.makedirs(output_dir, exist_ok=True)

    # 1. Mandelbrot
    m = compute_mandelbrot(size, size, max_iter=150)
    rgb_m = apply_colormap(m, palette="fire")
    p_m = os.path.join(output_dir, "mandelbrot_fire.png")
    Image.fromarray(rgb_m).save(p_m)

    # 2. Julia Set
    j = compute_julia(size, size, c_real=-0.7, c_imag=0.27015, max_iter=150)
    rgb_j = apply_colormap(j, palette="ocean")
    p_j = os.path.join(output_dir, "julia_ocean.png")
    Image.fromarray(rgb_j).save(p_j)

    # 3. Barnsley Fern
    fern = generate_barnsley_fern(num_points=120000, size=size)
    rgb_f = apply_colormap(fern, palette="twilight")
    p_f = os.path.join(output_dir, "barnsley_fern.png")
    Image.fromarray(rgb_f).save(p_f)

    print(f"Generated fractal previews in {output_dir}")


if __name__ == "__main__":
    generate_all_previews()
