# Fractal Geometry Generator & Explorer Suite

> **Proyek Capstone 7**: Aplikasi Pembangkit dan Visualisasi Interaktif Geometri Fraktal Klasik  
> **Program Studi**: S1 Ilmu Komputer / Informatika, FMIPA, Universitas Gadjah Mada  
> **Anggota Tim Pengembang**:  
> - Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
> - Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  

---

## Ringkasan Proyek
Aplikasi pembangkit dan penjelajah fraktal berkinerja tinggi berbasis vektorisasi NumPy untuk mengeksplorasi himpunan Mandelbrot, himpunan Julia, karpet Sierpinski, kepingan salju Koch, dan pakis Barnsley dengan *smooth continuous potential coloring* dan antarmuka interaktif desktop.

### Pembagian Tugas Tim 4 Mahasiswa
1. **Mahasiswa 1**: Pembangunan Mesin Bilangan Kompleks & Vektorisasi Mandelbrot/Julia.
2. **Mahasiswa 2**: Pembangkit Fraktal Geometris Rekursif (Sierpinski & Koch) dan Stokastik IFS (Barnsley Fern).
3. **Mahasiswa 3**: Modul Pewarnaan Halus (*Continuous Smooth Potential Color Mapping*) & Manajemen Palet.
4. **Mahasiswa 4**: Antarmuka Grafis (Tkinter GUI), Fitur Ekspor Citra, & Pengujian Kinerja Komputasi.

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
