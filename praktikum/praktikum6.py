from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Buka gambar background
background_path = r"C:\Users\kukohfr\Documents\Kuliah\Semester5\Pemrograman_Fungsional\Praktikum6\images\background.jpg"
background = Image.open(background_path)

# Buka gambar overlay
overlay_path = r"C:\Users\kukohfr\Documents\Kuliah\Semester5\Pemrograman_Fungsional\Praktikum6\images\overlay.png"
overlay = Image.open(overlay_path)

# Ubah gambar background menjadi hitam-putih, berotasi, dan blur
background = background.convert("L")
background = background.rotate(30)
background = background.filter(ImageFilter.BLUR)

# Resize gambar overlay sesuai kebutuhan
lebar = 100
tinggi = 100
overlay = overlay.resize((lebar, tinggi))

# Ubah tingkat kecerahan dan kontras gambar overlay
faktor_kecerahan = 1.01
faktor_kontras = 1.01
overlay = ImageEnhance.Brightness(overlay).enhance(faktor_kecerahan)
overlay = ImageEnhance.Contrast(overlay).enhance(faktor_kontras)

# Pastikan gambar overlay dalam mode RGBA agar dapat mempertahankan warna
overlay = overlay.convert("RGBA")

# Koordinat untuk menempatkan gambar overlay
x = 10
y = 10
posisi = (x, y)
background.paste(overlay, posisi, overlay)

# Menambahkan teks pada gambar overlay
gambar = ImageDraw.Draw(background)
path_font = r"C:\Users\kukohfr\Documents\Kuliah\Semester5\Pemrograman_Fungsional\Praktikum6\fonts\Arial.ttf"
font = ImageFont.truetype(path_font, 24)  # Gantilah dengan font yang sesuai

# Koordinat untuk menempatkan teks
x_teks = 100
y_teks = 80
posisi_teks = (x_teks, y_teks)
warna_teks = (0, 0, 255)  # Warna teks (RGB)
teks = "INFORMATIKA JOSSS!"
gambar.text(posisi_teks, teks, font=font, fill=warna_teks[0])

# Simpan gambar hasil edit
path_hasil = r"images\tugas_praktikum_enam.jpg"
background.save(path_hasil)

# Tampilkan gambar hasil edit
background.show()
