class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")

mhs1 = Mahasiswa("Zaki", "5240411230")

mhs1.tampilkan_info()


class Dompet:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal

    def tambah_uang(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil menambah Rp{jumlah}")
        else:
            print("Jumlah tidak valid.")

    def cek_saldo(self):
        print(f"Saldo Anda saat ini: Rp{self.__saldo}")


dompet_saya = Dompet(50000)
dompet_saya.cek_saldo()
dompet_saya.tambah_uang(20000)
dompet_saya.cek_saldo()


buku_judul = "Laskar Pelangi"
buku_penulis = "Andrea Hirata"

def tampilkan_buku(judul, penulis):
    print(f"Judul: {judul}")
    print(f"Penulis: {penulis}")

print("--- Info Buku (Prosedural) ---")
tampilkan_buku(buku_judul, buku_penulis)


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")


print("--- Info Buku (OOP) ---")
buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
buku1.tampilkan_info()
