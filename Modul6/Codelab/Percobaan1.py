# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()

image_path = "E:/Pratikum_Sem_5/Praktikum_Pemprograman_Fungsional_H/Modul6/Codelab/pasfoto.jpg"
gambarku = Image.open(image_path)

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype(r'E:\\Pratikum_Sem_5\Praktikum_Pemprograman_Fungsional_H\Modul6\Demo\arial.ttf',24)
text = "Abdul Karim-202110370311093"

text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('E:/Pratikum_Sem_5/Praktikum_Pemprograman_Fungsional_H/Modul6/percobaan_satu.jpg')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
