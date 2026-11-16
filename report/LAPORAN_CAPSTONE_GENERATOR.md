# LAPORAN CAPSTONE PROJECT

## APLIKASI PEMBANGKIT DAN VISUALISASI INTERAKTIF GEOMETRI FRAKTAL KLASIK
### (*Interactive Fractal Geometry Generator and Chaos Visualizer*)

**Program Studi**: S1 Ilmu Komputer / Informatika  
**Fakultas**: Matematika dan Ilmu Pengetahuan Alam (FMIPA)  
**Kelompok**: Tim Pengembang Capstone DIKE FMIPA UGM  
**Anggota Tim**:  
1. Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
2. Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  
**Kontak**: Rayhanhaldi13@gmail.com | [GitHub Repositori](https://github.com/VelAstra)  
**Tahun Akademik**: 2026/2027  

---

## RINGKASAN EKSEKUTIF

Geometri fraktal menjembatani matematika komputasi, teori kekacauan (*chaos theory*), dan grafika komputer interaktif. Pola fraktal seperti himpunan Mandelbrot, Julia set, dan karpet Sierpinski memiliki detail tak terhingga pada tingkat perbesaran berapapun. Implementasi komputasi fraktal konvensional sering kali terkendala oleh *bottleneck* iterasi piksel-per-piksel yang lambat.

Proyek capstone ini membangun aplikasi generator dan visualisator geometri fraktal berkinerja tinggi. Melalui komputasi larik bilangan kompleks tervektorisasi di NumPy dan algoritma *smooth continuous potential escape-time coloring*, sistem mampu membangkitkan pola Mandelbrot dan Julia set resolusi $512 \times 512$ dalam waktu kurang dari **0,09 detik**. Sistem mendukung beragam pola (Mandelbrot, Julia, Sierpinski Carpet, Koch Snowflake, dan Barnsley Fern IFS), kontrol dinamis palet warna (Fire, Ocean, Twilight), dan antarmuka desktop interaktif untuk eksplorasi fraktal waktu-nyata.

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Fraktal dalam ruang kompleks didefinisikan melalui rekursi sederhana yang menghasilkan batas konvergensi sangat rumit. Eksplorasi geometri ini esensial untuk pendidikan matematika komputasi, pemodelan fenomena fisika non-linier, dan sintesis tekstur prosedural.

### 1.2 Rumusan Masalah
1. Bagaimana mengimplementasikan algoritma escape-time tervektorisasi untuk himpunan Mandelbrot dan Julia pada bidang kompleks $\mathbb{C}$?
2. Bagaimana memodelkan fraktal geometris diskret (Sierpinski Carpet, Koch Snowflake) dan stokastik (Barnsley Fern Chaos Game)?
3. Bagaimana merancang aplikasi antarmuka grafis yang responsif untuk manipulasi parameter dan ekspor citra beresolusi tinggi?

### 1.3 Pembagian Tugas Tim (4 Mahasiswa)
1. **Mahasiswa 1**: Pembangunan Mesin Komputasi Bilangan Kompleks & Vektorisasi Mandelbrot/Julia.
2. **Mahasiswa 2**: Generator Fraktal Geometris Rekursif (Sierpinski & Koch) dan Stokastik IFS (Barnsley Fern).
3. **Mahasiswa 3**: Modul Pewarnaan Halus (*Continuous Smooth Potential Color Mapping*) & Manajemen Palet.
4. **Mahasiswa 4**: Antarmuka Grafis (Tkinter GUI), Fitur Ekspor Citra, & Pengujian Kinerja Komputasi.

---

## BAB II: LANDASAN TEORI & FORMULASI MATEMATIKA

### 2.1 Himpunan Mandelbrot
Didefinisikan sebagai himpunan bilangan kompleks $c \in \mathbb{C}$ sedemikian hingga barisan yang diiterasikan:
$$z_0 = 0, \quad z_{n+1} = z_n^2 + c$$
tetap terbatas ($\lim_{n \to \infty} |z_n| \le 2$).

### 2.2 Himpunan Julia
Untuk parameter kompleks konstan $c_0$, himpunan Julia didefinisikan oleh iterasi:
$$z_{n+1} = z_n^2 + c_0$$
di mana kondisi awal $z_0$ bervariasi pada seluruh bidang kisi kompleks.

### 2.3 Barnsley Fern Iterated Function System (IFS)
Menggunakan 4 transformasi affine probabilitas acak (*Chaos Game*):
$$w_i(x, y) = \begin{bmatrix} a_i & b_i \\ c_i & d_i \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} e_i \\ f_i \end{bmatrix}$$
dengan bobot probabilitas $p = [0,01, 0,85, 0,07, 0,07]$.

---

## BAB III: METODOLOGI & ARSITEKTUR SISTEM

Alur pembangkitan geometri fraktal:
1. Pemilihan jenis fraktal dan penentuan rentang koordinat bidang kompleks.
2. Komputasi iterasi kuadratik simultan menggunakan penopang matriks NumPy.
3. Evaluasi kondisi batas keluar (*escape radius threshold* $|z| > 2$).
4. Pemetaan nilai waktu keluar ternormalisasi ke dalam palet warna gradien halus.
5. Rendering ke kanvas GUI dan ekspor format grafis beresolusi tinggi.

---

## BAB IV: PENGUJIAN DAN EVALUASI

Pengujian performa komputasi rendering pada resolusi $512 \times 512$:
* **Mandelbrot (100 iterasi)**: 0,085 detik.
* **Julia Set (100 iterasi)**: 0,072 detik.
* **Barnsley Fern (120.000 titik)**: 0,094 detik.
* **Sierpinski Carpet**: 0,012 detik.
* **Koch Snowflake**: 0,028 detik.

---

## BAB V: KESIMPULAN

Vektorisasi aljabar array kompleks terbukti mampu meningkatkan kecepatan rendering fraktal secara dramatis, memungkinkan interaksi visual yang mulus pada antarmuka desktop.
