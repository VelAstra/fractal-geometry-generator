# Fractal Geometry Generator & Explorer Suite

> **Proyek Capstone 7**: Aplikasi Pembangkit dan Visualisasi Interaktif Geometri Fraktal Klasik  
> **Program Studi**: S1 Ilmu Komputer / Informatika, FMIPA, Universitas Gadjah Mada  
> **Anggota Tim Pengembang**:  
> - Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
> - Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  

---

## Ringkasan Proyek
Aplikasi pembangkit dan penjelajah fraktal berkinerja tinggi berbasis vektorisasi NumPy untuk mengeksplorasi himpunan Mandelbrot, himpunan Julia, karpet Sierpinski, kepingan salju Koch, dan pakis Barnsley dengan *smooth continuous potential coloring* dan antarmuka interaktif desktop.

### Pembagian Tugas Tim (2 Mahasiswa)
1. **Aji Kusuma Putra** (`22/503701/PA/21657`): Mesin komputasi bidang bilangan kompleks, vektorisasi Mandelbrot/Julia, generator geometri rekursif (Sierpinski, Koch), dan generator stokastik IFS Barnsley Fern (Chaos Game). (Modul: `core/mandelbrot.py`, `core/geometric_fractals.py`).
2. **Rayhan Haldi Hermawan** (`24/545406/PA/23176`): Modul pewarnaan continuous potential escape-time, manajemen palet warna dinamis, Desktop GUI Tkinter, navigasi zoom interaktif, ekspor citra resolusi tinggi, integrasi CLI, dan benchmark throughput. (Modul: `core/color_maps.py`, `sample_data/generate_previews.py`, `gui/app.py`, `cli.py`).

---

## Cara Menjalankan

```bash
# Merender fraktal Mandelbrot resolusi 512x512
python cli.py render --type mandelbrot --size 512 --palette fire

# Merender Julia set dengan palet ocean
python cli.py render --type julia --size 512 --palette ocean

# Menjalankan antarmuka grafis
python cli.py gui

# Menjalankan uji otomatis
python -m unittest discover tests
```
