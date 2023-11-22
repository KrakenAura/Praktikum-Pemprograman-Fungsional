import math

def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        new_x = x + tx
        new_y = y + ty
        return (new_x, new_y)
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        new_x = x * sx
        new_y = y * sy
        return (new_x, new_y)
    return transformasi

def rotasi(sudut):
    def transformasi(p):
        x, y = p
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return (new_x, new_y)
    return transformasi

def tampilkan_koordinat(p, label):
    print(f"{label}: {p[0]:.6f}, {p[1]:.6f}")

# Titik awal P
titik_P = (3, 5)

# Translasi
translasi_func = translasi(tx=2, ty=-1)
titik_setelah_translasi = translasi_func(titik_P)

# Dilatasi
dilatasi_func = dilatasi(sx=2, sy=-1)
titik_setelah_dilatasi = dilatasi_func(titik_P)

# Rotasi
rotasi_func = rotasi(sudut=30)
titik_setelah_rotasi = rotasi_func(titik_P)

# Menampilkan hasil
tampilkan_koordinat(titik_setelah_translasi, "Koordinat setelah translasi")
tampilkan_koordinat(titik_setelah_dilatasi, "Koordinat setelah dilatasi")
tampilkan_koordinat(titik_setelah_rotasi, "Koordinat setelah rotasi")