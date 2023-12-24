from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont


#TODO Membuka gambar dengan Pillow
background = Image.open(r'E:\Pratikum_Sem_5\Praktikum_Pemprograman_Fungsional_H\Modul6\Demo\background.jpeg')
overlay = Image.open(r'E:\Pratikum_Sem_5\Praktikum_Pemprograman_Fungsional_H\Modul6\Demo\Overlay.jpeg')

#TODO Modifikasi Background (grayscale, rotasi 30, blur)
background_grayscale = background.convert("L")
background_rotated = background_grayscale.rotate(30)
background_blurred = background_rotated.filter(ImageFilter.GaussianBlur(radius=2))

#TODO Ubah Kecerahan dan Kontras Overlay menjadi 1.(2 digit NIM) , Resize
kecerahan = 1.9
kontras = 1.3
overlay_brightness = ImageEnhance.Brightness(overlay).enhance(kecerahan)
overlay_contrast = ImageEnhance.Contrast(overlay_brightness).enhance(kontras)
ukuran = (500,500)
overlay_resize = overlay_contrast.resize(ukuran)

#TODO Sisipkan gambar overlay ke dalam background
x_tengah = (background.width - overlay.width) // 2
y_tengah = (background.height - overlay.height) // 2
background_blurred.paste(overlay_resize,(x_tengah,y_tengah))

#TODO Tambahkan teks "Informatika JOSSS!" (Arial,24)
draw = ImageDraw.Draw(background_blurred)
font = ImageFont.truetype(r'E:\\Pratikum_Sem_5\Praktikum_Pemprograman_Fungsional_H\Modul6\Demo\arial.ttf',24)
text = "Informatika JOSSS!"

# hasil_akhir = draw.text((x_tengah,0), text, font=font, fill=255)
draw.text((x_tengah,50), text, font=font, fill=255)

#TODO Simpan gambar dengan hasil edit "tugas_praktikum_enam.jpg"
background_blurred.save("tugas_praktikum_enam.jpg")
