#Sistem Penilaian Akhir Mahasiswa

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(UTS, UAS):
    return (UTS + UAS) / 2

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def nilai_akhir_semua(data_mahasiswa):
    for nama, nilai in data_mahasiswa.items():
        nilai['Nilai'] = hitung_nilai_akhir(nilai['UTS'], nilai['UAS'])
    return data_mahasiswa

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def tambah_mahasiswa(data_mahasiswa, nama, UTS, UAS):
    data_mahasiswa[nama] = {'UTS': UTS, 'UAS': UAS}

def main():
    data_mahasiswa = {}
    tambah_mahasiswa(data_mahasiswa, 'Karim', 90, 80)
    tambah_mahasiswa(data_mahasiswa, 'Abdul', 90, 80)
    tambah_mahasiswa(data_mahasiswa, 'Alpha', 90, 80)

    nilai_akhir_semua(data_mahasiswa)

    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        data_nilai_akhir[nama] = nilai['Nilai']

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
