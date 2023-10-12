# Fungsi untuk input buku
def input_buku(data_buku, judul):
    data_buku[judul] = {"Peminjam": None}

#Fungsi untuk pinjam buku
def pinjam_buku(data_buku, judul, peminjam):
    if judul in data_buku:
        if data_buku[judul]["Peminjam"] is None:
            data_buku[judul]["Peminjam"] = peminjam
            print("Buku", judul, "berhasil dipinjam oleh", peminjam)
        else:
            print("Maaf buku", judul, "sedang dipinjam oleh", data_buku[judul]["Peminjam"])
    else:
        print("Maaf buku", judul, "tidak ada")

def main():
    loop = 1
    data_buku = {}
    
    while loop == 1:
        print("Selamat Datang di Program Peminjaman Buku")
        print("Silahkan pilih menu:")
        print("1. Admin")
        print("2. User")
        print("3. List Buku")
        print("4. Quit")
        menu = input("Pilih Menu: ")

        if menu == "1":
            judul = input("Masukkan judul buku: ")
            input_buku(data_buku, judul)
        elif menu == "2":
            judul = input("Masukkan judul buku: ")
            peminjam = input("Masukkan nama peminjam: ")
            pinjam_buku(data_buku, judul, peminjam)
        elif menu == "3":
            print("Daftar Buku:")
            for judul, info in data_buku.items():
                peminjam = info["Peminjam"]
                status = "tersedia" if peminjam is None else f"dipinjam oleh {peminjam}"
                print(f"{judul}: {status}")
        elif menu == "4":
            loop = 0
        else:
            print("Menu tidak ditemukan")

if __name__ == "__main__":
    main()
