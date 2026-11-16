"""
Interactive Fractal Geometry Visualizer and Explorer GUI.
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk

from core.mandelbrot import compute_mandelbrot, compute_julia
from core.geometric_fractals import generate_sierpinski_carpet, generate_barnsley_fern, generate_koch_snowflake
from core.color_maps import apply_colormap


class FractalExplorerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fractal Geometry Explorer Studio")
        self.geometry("980x680")
        self.configure(bg="#0B0F19")

        self.current_rgb = None
        self.tk_img = None

        self._build_ui()
        self.on_render()

    def _build_ui(self):
        header = tk.Frame(self, bg="#1E1B4B", height=60, padx=20)
        header.pack(fill=tk.X)
        tk.Label(header, text="FRACTAL GEOMETRY GENERATOR & VISUALIZER", font=("Segoe UI", 13, "bold"), fg="#A78BFA", bg="#1E1B4B").pack(anchor="w", pady=(10, 0))
        tk.Label(header, text="Eksplorasi Himpunan Mandelbrot, Julia Set, Sierpinski, dan Koch Snowflake", font=("Segoe UI", 9), fg="#C4B5FD", bg="#1E1B4B").pack(anchor="w")

        controls = tk.Frame(self, bg="#111827", padx=15, pady=10)
        controls.pack(fill=tk.X)

        tk.Label(controls, text="Jenis Fraktal:", bg="#111827", fg="#F3F4F6", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=(0, 4))
        self.type_var = tk.StringVar(value="mandelbrot")
        cb_type = ttk.Combobox(controls, textvariable=self.type_var, values=["mandelbrot", "julia", "carpet", "fern", "snowflake"], width=12, state="readonly")
        cb_type.pack(side=tk.LEFT, padx=(0, 15))

        tk.Label(controls, text="Palet Warna:", bg="#111827", fg="#F3F4F6", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=(0, 4))
        self.palette_var = tk.StringVar(value="fire")
        cb_pal = ttk.Combobox(controls, textvariable=self.palette_var, values=["fire", "ocean", "twilight", "monochrome"], width=10, state="readonly")
        cb_pal.pack(side=tk.LEFT, padx=(0, 15))

        tk.Label(controls, text="Iterasi:", bg="#111827", fg="#F3F4F6", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=(0, 4))
        self.iter_var = tk.IntVar(value=100)
        scale_it = tk.Scale(controls, from_=20, to=300, orient=tk.HORIZONTAL, variable=self.iter_var, bg="#111827", fg="#F3F4F6", highlightthickness=0, length=90)
        scale_it.pack(side=tk.LEFT, padx=(0, 15))

        ttk.Button(controls, text="Bangkitkan Fraktal", command=self.on_render).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls, text="Simpan PNG...", command=self.on_save).pack(side=tk.LEFT, padx=5)

        # Center Canvas
        self.canvas_lbl = tk.Label(self, bg="#030712")
        self.canvas_lbl.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Status
        self.status = tk.Label(self, text="Siap.", bg="#1E1B4B", fg="#E0E7FF", anchor="w", padx=10, font=("Segoe UI", 9))
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

    def on_render(self):
        ftype = self.type_var.get()
        pal = self.palette_var.get()
        iters = self.iter_var.get()
        size = 460

        self.status.config(text=f"Membangkitkan {ftype}...")
        self.update_idletasks()

        if ftype == "mandelbrot":
            data = compute_mandelbrot(size, size, max_iter=iters)
        elif ftype == "julia":
            data = compute_julia(size, size, max_iter=iters)
        elif ftype == "carpet":
            data = generate_sierpinski_carpet(size=size)
        elif ftype == "fern":
            data = generate_barnsley_fern(size=size)
        elif ftype == "snowflake":
            data = generate_koch_snowflake(size=size)
        else:
            data = compute_mandelbrot(size, size)

        rgb = apply_colormap(data, palette=pal)
        self.current_rgb = rgb

        pil_img = Image.fromarray(rgb)
        self.tk_img = ImageTk.PhotoImage(pil_img)
        self.canvas_lbl.config(image=self.tk_img)
        self.status.config(text=f"Selesai: {ftype.upper()} ({size}x{size}, Palet: {pal}, Iterasi: {iters})")

    def on_save(self):
        if self.current_rgb is None:
            return
        f = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if f:
            Image.fromarray(self.current_rgb).save(f)
            messagebox.showinfo("Berhasil", f"Citra fraktal disimpan di {f}")


def launch_gui():
    app = FractalExplorerApp()
    app.mainloop()


if __name__ == "__main__":
    launch_gui()
