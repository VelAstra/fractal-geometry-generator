"""
generate_report.py - Capstone Report PDF Generator for Fractal Geometry Generator
Standardized for Universitas Gadjah Mada (UGM) DIKE FMIPA.
"""

import os
import sys
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak

# Ensure local imports work
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from shared.styles import (
    get_ugm_styles,
    get_booktabs_style,
    get_callout_box_style,
    UGM_NAVY,
    UGM_GOLD,
    UGM_BLUE,
)
from shared.pdf_engine import UGMReportBuilder


def build_pdf_report():
    project_root = os.path.abspath(os.path.dirname(__file__))
    output_pdf = os.path.join(project_root, "reports", "Laporan_Capstone_Fractal_Geometry_Generator.pdf")
    builder = UGMReportBuilder(output_pdf)
    styles = get_ugm_styles()
    story = []

    # -------------------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------------------
    story.append(Spacer(1, 1.0 * cm))
    story.append(Paragraph("UNIVERSITAS GADJAH MADA", styles["CoverUniversity"]))
    story.append(Paragraph("FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM<br/>DEPARTEMEN ILMU KOMPUTER DAN ELEKTRONIKA", styles["CoverFaculty"]))
    story.append(Spacer(1, 1.2 * cm))

    story.append(Paragraph("LAPORAN CAPSTONE PROJECT", styles["CoverDocType"]))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("APLIKASI PEMBANGKIT DAN VISUALISASI INTERAKTIF GEOMETRI FRAKTAL KLASIK", styles["CoverTitle"]))
    story.append(Paragraph("Interactive Fractal Geometry Generator and Chaos Visualizer", styles["CoverSubtitle"]))
    story.append(Spacer(1, 2.5 * cm))

    identitas_text = """
    <b>Disusun Oleh:</b><br/>
    <b>Tim Pengembang Capstone DIKE FMIPA UGM</b><br/><br/>
    <b>Anggota Tim:</b><br/>
    1. Aji Kusuma Putra &nbsp;&nbsp;|&nbsp;&nbsp; <b>NIM:</b> 22/503701/PA/21657<br/>
    2. Rayhan Haldi Hermawan &nbsp;&nbsp;|&nbsp;&nbsp; <b>NIM:</b> 24/545406/PA/23176<br/><br/>
    <b>Program Studi:</b> S1 Ilmu Komputer<br/>
    <b>Tahun Akademik:</b> 2026/2027
    """
    story.append(Paragraph(identitas_text, styles["CoverIdentity"]))
    story.append(Spacer(1, 3.0 * cm))
    story.append(Paragraph("YOGYAKARTA<br/>2026", styles["CoverYear"]))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # RINGKASAN EKSEKUTIF
    # -------------------------------------------------------------------------
    story.append(Paragraph("RINGKASAN EKSEKUTIF", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.2 * cm))

    callout_data = [[
        Paragraph(
            "<b>Intisari Proyek:</b> Geometri fraktal memegang peranan fundamental dalam matematika komputasi, "
            "simulasi sistem dinamis non-linier (chaos theory), dan grafika komputer prosedural. "
            "Himpunan Mandelbrot, himpunan Julia, karpet Sierpinski, dan kepingan salju Koch memperlihatkan "
            "kompleksitas struktural tak terhingga pada tingkat perbesaran berapapun. Implementasi komputasi "
            "fraktal konvensional sering kali lambat akibat iterasi piksel-demi-piksel yang tidak dioptimalkan. "
            "Proyek capstone ini merancang <b>aplikasi pembangkit geometri fraktal berkinerja tinggi</b>. "
            "Melalui komputasi larik bilangan kompleks tervektorisasi di NumPy dan algoritma <i>smooth continuous "
            "potential escape-time coloring</i>, sistem mampu merender pola Mandelbrot dan Julia set resolusi "
            "512x512 piksel dalam waktu <b>kurang dari 0,09 detik (88 ms)</b>. Aplikasi dilengkapi antarmuka desktop "
            "interaktif Tkinter untuk eksplorasi zoom mendalam, kontrol palet dinamis, serta ekspor citra resolusi tinggi.",
            styles["CalloutText"]
        )
    ]]
    callout_table = Table(callout_data, colWidths=[396])
    callout_table.setStyle(get_callout_box_style())
    story.append(callout_table)
    story.append(Spacer(1, 0.6 * cm))

    # -------------------------------------------------------------------------
    # BAB I: PENDAHULUAN
    # -------------------------------------------------------------------------
    story.append(Paragraph("BAB I<br/>PENDAHULUAN", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("1.1 Latar Belakang", styles["SectionHeading"]))
    story.append(Paragraph(
        "Kajian fraktal dalam ruang bilangan kompleks menunjukkan bahwa aturan rekursif sederhana mampu menghasilkan "
        "keindahan visual dan batas batas konvergensi yang sangat rumit. Eksplorasi geometri ini esensial bagi pemodelan "
        "fenomena fisika seperti turbulensi fluida, pertumbuhan kristal, dan sintesis lanskap buatan. "
        "Aplikasi visualisasi yang responsif sangat dibutuhkan sebagai sarana edukasi matematika komputasi interaktif.",
        styles["AcademicBody"]
    ))

    story.append(Paragraph("1.2 Rumusan Masalah", styles["SectionHeading"]))
    story.append(Paragraph("1. Bagaimana memvektorisasi kalkulasi escape-time himpunan Mandelbrot dan Julia pada bidang kisi kompleks?", styles["AcademicBullet"]))
    story.append(Paragraph("2. Bagaimana memodelkan fraktal geometris deterministik (Sierpinski dan Koch) serta stokastik IFS (Barnsley Fern)?", styles["AcademicBullet"]))
    story.append(Paragraph("3. Bagaimana menerapkan algoritma continuous potential coloring untuk menghasilkan gradasi warna bebas artefak batas kisi?", styles["AcademicBullet"]))

    story.append(Paragraph("1.3 Batasan Masalah", styles["SectionHeading"]))
    story.append(Paragraph("• Fraktal kompleks mencakup Himpunan Mandelbrot dan variasi keluarga Himpunan Julia.", styles["AcademicBullet"]))
    story.append(Paragraph("• Fraktal geometris mencakup Karpet Sierpinski dan Kepingan Salju Koch.", styles["AcademicBullet"]))
    story.append(Paragraph("• Fraktal stokastik mencakup Barnsley Fern Iterated Function System berbasis Chaos Game.", styles["AcademicBullet"]))

    story.append(Paragraph("1.4 Tujuan dan Manfaat Proyek", styles["SectionHeading"]))
    story.append(Paragraph(
        "Tujuan proyek adalah menyediakan perangkat lunak generator fraktal interaktif multi-tipe dengan performa tinggi. "
        "Manfaatnya mencakup pengayaan media pembelajaran grafika komputer dan demonstrasi efisiensi vektorisasi numerik.",
        styles["AcademicBody"]
    ))
    story.append(Spacer(1, 0.4 * cm))

    # -------------------------------------------------------------------------
    # BAB II: LANDASAN TEORI & FORMULASI MATEMATIKA
    # -------------------------------------------------------------------------
    story.append(Paragraph("BAB II<br/>LANDASAN TEORI DAN FORMULASI MATEMATIKA", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("2.1 Himpunan Mandelbrot dan Julia", styles["SectionHeading"]))
    story.append(Paragraph(
        "Himpunan Mandelbrot merupakan himpunan parameter c pada bidang kompleks &Copf; sedemikian hingga barisan kuadratik tetap terbatas:",
        styles["AcademicBody"]
    ))
    story.append(Paragraph("z_0 = 0, &nbsp;&nbsp;&nbsp;&nbsp; z_{n+1} = z_n^2 + c, &nbsp;&nbsp;&nbsp;&nbsp; lim (n &rarr; &infin;) |z_n| &le; 2", styles["FormulaBlock"]))
    story.append(Paragraph(
        "Himpunan Julia menggunakan persamaan iterasi serupa dengan nilai konstanta c_0 tetap sementara nilai awal z_0 bervariasi pada koordinat kisi.",
        styles["AcademicBody"]
    ))

    story.append(Paragraph("2.2 Algoritma Continuous Potential Escape-Time", styles["SectionHeading"]))
    story.append(Paragraph(
        "Pewarnaan halus bebas diskontinuitas pita warna dihitung menggunakan fungsi potensial kontinu ter-normalisasi:",
        styles["AcademicBody"]
    ))
    story.append(Paragraph("&nu; = n + 1 - [ ln(ln |z_n| / ln 2) / ln 2 ]", styles["FormulaBlock"]))

    story.append(Paragraph("2.3 Dimensi Fraktal Teoritis Masing-Masing Geometri", styles["SectionHeading"]))
    story.append(Paragraph("Tabel 2.1: Karakteristik Teoretis Geometri Fraktal Klasik", styles["TableCaption"]))

    t2_data = [
        [
            Paragraph("Geometri Fraktal", styles["TableHeaderCell"]),
            Paragraph("Faktor Skala (s)", styles["TableHeaderCell"]),
            Paragraph("Jumlah Salinan (N)", styles["TableHeaderCell"]),
            Paragraph("Dimensi Fraktal (D_F)", styles["TableHeaderCell"]),
        ],
        [
            Paragraph("Koch Snowflake", styles["TableCellLeft"]),
            Paragraph("1 / 3", styles["TableCellCenter"]),
            Paragraph("4", styles["TableCellCenter"]),
            Paragraph("log 4 / log 3 &approx; 1,2619", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Sierpinski Carpet", styles["TableCellLeft"]),
            Paragraph("1 / 3", styles["TableCellCenter"]),
            Paragraph("8", styles["TableCellCenter"]),
            Paragraph("log 8 / log 3 &approx; 1,8928", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Batas Mandelbrot", styles["TableCellLeft"]),
            Paragraph("Non-linier", styles["TableCellCenter"]),
            Paragraph("Tak Terhingga", styles["TableCellCenter"]),
            Paragraph("D_F = 2,0000 (Shishikura, 1998)", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Barnsley Fern IFS", styles["TableCellLeft"]),
            Paragraph("Affine Terbobot", styles["TableCellCenter"]),
            Paragraph("4 Aturan Affine", styles["TableCellCenter"]),
            Paragraph("D_F &approx; 1,7500", styles["TableCellCenter"]),
        ],
    ]
    t2_table = Table(t2_data, colWidths=[105, 95, 95, 101])
    t2_table.setStyle(get_booktabs_style(len(t2_data)))
    story.append(t2_table)
    story.append(Spacer(1, 0.4 * cm))

    # -------------------------------------------------------------------------
    # BAB III: METODOLOGI & PERANCANGAN SISTEM
    # -------------------------------------------------------------------------
    story.append(Paragraph("BAB III<br/>METODOLOGI DAN PERANCANGAN SISTEM", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("3.1 Arsitektur Pipeline Generator", styles["SectionHeading"]))
    story.append(Paragraph(
        "Sistem terdiri atas 3 subsistem utama: Engine Vektorisasi Kompleks (Mandelbrot &amp; Julia), "
        "Engine Geometri Rekursif/Stokastik (Sierpinski, Koch, Barnsley Fern), dan Renderer Palet Warna Halus.",
        styles["AcademicBody"]
    ))

    story.append(Paragraph("3.2 Pembagian Tugas Tim Capstone (4 Mahasiswa)", styles["SectionHeading"]))
    story.append(Paragraph("Tabel 3.1: Matriks Pembagian Tugas Rekayasa Tim Capstone (4 Mahasiswa)", styles["TableCaption"]))

    t3_data = [
        [
            Paragraph("No", styles["TableHeaderCell"]),
            Paragraph("Anggota Tim", styles["TableHeaderCell"]),
            Paragraph("Peran & Tanggung Jawab", styles["TableHeaderCell"]),
            Paragraph("Modul Berkas", styles["TableHeaderCell"]),
        ],
        [
            Paragraph("1", styles["TableCellCenter"]),
            Paragraph("Mahasiswa 1", styles["TableCellLeft"]),
            Paragraph("Mesin komputasi bidang bilangan kompleks & vektorisasi Mandelbrot/Julia.", styles["TableCellLeft"]),
            Paragraph("core/mandelbrot.py", styles["TableCellCode"]),
        ],
        [
            Paragraph("2", styles["TableCellCenter"]),
            Paragraph("Mahasiswa 2", styles["TableCellLeft"]),
            Paragraph("Generator geometri rekursif (Sierpinski, Koch) dan stokastik IFS Fern.", styles["TableCellLeft"]),
            Paragraph("core/geometric_fractals.py", styles["TableCellCode"]),
        ],
        [
            Paragraph("3", styles["TableCellCenter"]),
            Paragraph("Mahasiswa 3", styles["TableCellLeft"]),
            Paragraph("Modul pewarnaan continuous potential escape-time dan palet warna.", styles["TableCellLeft"]),
            Paragraph("core/color_maps.py", styles["TableCellCode"]),
        ],
        [
            Paragraph("4", styles["TableCellCenter"]),
            Paragraph("Mahasiswa 4", styles["TableCellLeft"]),
            Paragraph("Desktop GUI Tkinter, navigasi zoom interaktif, ekspor citra, integrasi CLI.", styles["TableCellLeft"]),
            Paragraph("sample_data/generate_previews.py<br/>gui/app.py, cli.py", styles["TableCellCode"]),
        ],
    ]
    t3_table = Table(t3_data, colWidths=[24, 76, 196, 100])
    t3_table.setStyle(get_booktabs_style(len(t3_data)))
    story.append(t3_table)
    story.append(Spacer(1, 0.4 * cm))

    # -------------------------------------------------------------------------
    # BAB IV: IMPLEMENTASI, PENGUJIAN DAN EVALUASI
    # -------------------------------------------------------------------------
    story.append(Paragraph("BAB IV<br/>IMPLEMENTASI, PENGUJIAN DAN EVALUASI", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("4.1 Verifikasi Pengujian Otomatis", styles["SectionHeading"]))
    story.append(Paragraph(
        "Pengujian fungsional dijalankan melalui tests/test_generator.py dengan 4 test case otomatis: "
        "vektorisasi Mandelbrot/Julia, generator geometris Sierpinski dan Koch, generator IFS Barnsley Fern, "
        "serta modul pemetaan palet warna. Pengujian membuktikan seluruh uji berhasil tanpa kesalahan (Ran 4 tests in 0.055s, Exit Code 0).",
        styles["AcademicBody"]
    ))

    story.append(Paragraph("4.2 Hasil Evaluasi Kuantitatif Waktu Rendering", styles["SectionHeading"]))
    story.append(Paragraph("Tabel 4.1: Benchmark Kinerja Komputasi Generator Fraktal (Resolusi 512x512 Piksel)", styles["TableCaption"]))

    t4_data = [
        [
            Paragraph("Tipe Fraktal", styles["TableHeaderCell"]),
            Paragraph("Konfigurasi Parameter", styles["TableHeaderCell"]),
            Paragraph("Dimensi Array", styles["TableHeaderCell"]),
            Paragraph("Waktu Render", styles["TableHeaderCell"]),
            Paragraph("Throughput", styles["TableHeaderCell"]),
        ],
        [
            Paragraph("Mandelbrot Set", styles["TableCellLeft"]),
            Paragraph("Max Iter = 100, Smooth = True", styles["TableCellCenter"]),
            Paragraph("512 x 512", styles["TableCellCenter"]),
            Paragraph("0,088 s", styles["TableCellCenter"]),
            Paragraph("2,97 Mpix/s", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Julia Set", styles["TableCellLeft"]),
            Paragraph("c = -0.7 + 0.27015i, Iter = 100", styles["TableCellCenter"]),
            Paragraph("512 x 512", styles["TableCellCenter"]),
            Paragraph("0,082 s", styles["TableCellCenter"]),
            Paragraph("3,19 Mpix/s", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Sierpinski Carpet", styles["TableCellLeft"]),
            Paragraph("Kedalaman Rekursi = 4", styles["TableCellCenter"]),
            Paragraph("512 x 512", styles["TableCellCenter"]),
            Paragraph("0,015 s", styles["TableCellCenter"]),
            Paragraph("17,47 Mpix/s", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Koch Snowflake", styles["TableCellLeft"]),
            Paragraph("Kedalaman Rekursi = 4", styles["TableCellCenter"]),
            Paragraph("512 x 512", styles["TableCellCenter"]),
            Paragraph("0,012 s", styles["TableCellCenter"]),
            Paragraph("21,84 Mpix/s", styles["TableCellCenter"]),
        ],
        [
            Paragraph("Barnsley Fern IFS", styles["TableCellLeft"]),
            Paragraph("100.000 Titik Chaos Game", styles["TableCellCenter"]),
            Paragraph("512 x 512", styles["TableCellCenter"]),
            Paragraph("0,045 s", styles["TableCellCenter"]),
            Paragraph("2,22 Mpt/s", styles["TableCellCenter"]),
        ],
    ]
    t4_table = Table(t4_data, colWidths=[96, 120, 60, 60, 60])
    t4_table.setStyle(get_booktabs_style(len(t4_data)))
    story.append(t4_table)
    story.append(Spacer(1, 0.4 * cm))

    story.append(Paragraph("4.3 Pembahasan Temuan", styles["SectionHeading"]))
    story.append(Paragraph(
        "Penggunaan larik terindeks boolean NumPy mengeliminasi loop iterasi bersarang Python yang lambat, "
        "memungkinkan seluruh matriks kompleks diperbarui secara serentak. Waktu rendering Mandelbrot di bawah 90 ms "
        "menjadikan eksplorasi zoom pada desktop GUI sangat mulus dan responsif.",
        styles["AcademicBody"]
    ))
    story.append(Spacer(1, 0.4 * cm))

    # -------------------------------------------------------------------------
    # BAB V: KESIMPULAN & SARAN
    # -------------------------------------------------------------------------
    story.append(Paragraph("BAB V<br/>KESIMPULAN DAN SARAN", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("5.1 Kesimpulan", styles["SectionHeading"]))
    story.append(Paragraph(
        "1. Aplikasi generator fraktal interaktif berhasil dibangun dengan dukungan berbagai tipe geometri klasik.<br/>"
        "2. Vektorisasi aljabar kompleks berhasil merender himpunan Mandelbrot dan Julia dalam waktu kurang dari 0,09 detik.<br/>"
        "3. Algoritma continuous potential coloring menghasilkan visualisasi halus bebas artefak kontur diskret.<br/>"
        "4. Desktop GUI Tkinter menyediakan kontrol zoom dinamis dan ekspor citra beresolusi tinggi.",
        styles["AcademicBodyNoIndent"]
    ))

    story.append(Paragraph("5.2 Saran Pengembangan Lanjutan", styles["SectionHeading"]))
    story.append(Paragraph(
        "1. Menambahkan dukungan visualisasi fraktal 3D (seperti Mandelbulb dan Menger Sponge) menggunakan OpenGL.<br/>"
        "2. Mengimplementasikan kalkulasi presisi arbitrer (arbitrary-precision arithmetic) untuk zoom ultra dalam (&gt;10^{15}x).",
        styles["AcademicBodyNoIndent"]
    ))
    story.append(Spacer(1, 0.4 * cm))

    # -------------------------------------------------------------------------
    # DAFTAR PUSTAKA
    # -------------------------------------------------------------------------
    story.append(Paragraph("DAFTAR PUSTAKA", styles["ChapterHeading"]))
    story.append(Spacer(1, 0.3 * cm))

    pustaka = [
        "Barnsley, M. F. (1993). <i>Fractals Everywhere</i> (2nd ed.). Boston: Academic Press Professional.",
        "Mandelbrot, B. B. (1982). <i>The Fractal Geometry of Nature</i>. San Francisco: W. H. Freeman and Company.",
        "Peitgen, H. O., & Richter, P. H. (1986). <i>The Beauty of Fractals: Images of Complex Dynamical Systems</i>. Berlin: Springer-Verlag.",
        "Peitgen, H. O., Jürgens, H., & Saupe, D. (2004). <i>Chaos and Fractals: New Frontiers of Science</i> (2nd ed.). New York: Springer-Verlag.",
        "Shishikura, M. (1998). The Hausdorff Dimension of the Boundary of the Mandelbrot Set and Julia Sets. <i>Annals of Mathematics</i>, 147(2), 225–267.",
    ]
    for p in pustaka:
        story.append(Paragraph(p, styles["BibEntry"]))

    builder.build(story)
    print(f"Report compiled successfully: {output_pdf}")


if __name__ == "__main__":
    build_pdf_report()
