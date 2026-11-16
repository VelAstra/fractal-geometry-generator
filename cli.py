"""
CLI for Fractal Geometry Generator Suite.
"""

import argparse
import sys
import os
import time
from PIL import Image

from core.mandelbrot import compute_mandelbrot, compute_julia
from core.geometric_fractals import generate_sierpinski_carpet, generate_barnsley_fern, generate_koch_snowflake
from core.color_maps import apply_colormap


def cmd_render(args):
    print(f"[Fractal Generator] Membangkitkan fraktal: {args.type} ({args.size}x{args.size})")
    t0 = time.perf_counter()

    if args.type == "mandelbrot":
        data = compute_mandelbrot(args.size, args.size, max_iter=args.iters)
    elif args.type == "julia":
        data = compute_julia(args.size, args.size, c_real=args.cr, c_imag=args.ci, max_iter=args.iters)
    elif args.type == "carpet":
        data = generate_sierpinski_carpet(size=args.size)
    elif args.type == "fern":
        data = generate_barnsley_fern(size=args.size)
    elif args.type == "snowflake":
        data = generate_koch_snowflake(size=args.size)
    else:
        data = compute_mandelbrot(args.size, args.size)

    rgb = apply_colormap(data, palette=args.palette)
    render_time = time.perf_counter() - t0

    out_path = args.output or f"sample_data/{args.type}_{args.palette}.png"
    Image.fromarray(rgb).save(out_path)

    print(f"Hasil rendering tersimpan di : {out_path}")
    print(f"Waktu Komputasi Rendering    : {render_time:.3f} detik")


def cmd_gui(args):
    from gui.app import launch_gui
    launch_gui()


def main():
    p = argparse.ArgumentParser(description="Fractal Geometry Generator")
    sub = p.add_subparsers(dest="command")

    p_ren = sub.add_parser("render", help="Render a fractal image")
    p_ren.add_argument("--type", default="mandelbrot", choices=["mandelbrot", "julia", "carpet", "fern", "snowflake"])
    p_ren.add_argument("--size", type=int, default=512)
    p_ren.add_argument("--iters", type=int, default=100)
    p_ren.add_argument("--palette", default="fire", choices=["fire", "ocean", "twilight", "monochrome"])
    p_ren.add_argument("--cr", type=float, default=-0.7, help="Julia real constant")
    p_ren.add_argument("--ci", type=float, default=0.27015, help="Julia imag constant")
    p_ren.add_argument("-o", "--output")

    sub.add_parser("gui", help="Launch interactive explorer GUI")

    args = p.parse_args()
    if args.command == "render":
        cmd_render(args)
    elif args.command == "gui":
        cmd_gui(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
