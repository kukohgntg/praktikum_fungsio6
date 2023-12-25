# Lengkapi kode dibawah untuk menjawab soal diatas ya
# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open(
    r"C:\Users\kukohfr\Documents\Kuliah\Semester5\Pemrograman_Fungsional\Praktikum6\images\lambang_umm.png")

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font_path = r"C:\Users\kukohfr\Documents\Kuliah\Semester5\Pemrograman_Fungsional\Praktikum6\fonts\Arial.ttf"
font_size = 24

# Try to load the font

font = ImageFont.truetype(font_path, font_size)

text = "Nama: Kukoh Fatchu Rahman\nNIM: 202110370311001"

# Get the size of the text bounding box using the font object
text_bbox = draw.textbbox((0, 0), text, font)
text_width, text_height = text_bbox[2] - \
    text_bbox[0], text_bbox[3] - text_bbox[1]

# Calculate the center position
center_x = (gambarku.width - text_width) // 2
center_y = (gambarku.height - text_height) // 2

draw.text((center_x, center_y), text, font=font)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("images\percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
