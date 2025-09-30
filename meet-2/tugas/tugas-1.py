class KoneksiDatabase:
    def __init__(self, nama_db):
        print("--- [INIT] Memulai koneksi... ---")
        self.nama_db = nama_db
        self.terhubung = True
        print(f"Koneksi ke database '{self.nama_db}' berhasil DIBUAT.")

    def kirim_data(self, data):
        if self.terhubung:
            print(f"Mengirim data '{data}' ke database '{self.nama_db}'...")
        else:
            print("Koneksi sudah ditutup!")

    def __del__(self):
        print("--- [DEL] Membersihkan... ---")
        self.terhubung = False
        print(f"Koneksi ke database '{self.nama_db}' telah DITUTUP.")


print("Membuat object koneksi...")
db = KoneksiDatabase("TokoOnlineDB")

print("\nMenggunakan object...")
db.kirim_data("Sepatu Baru")

print("\nMenghapus object...")
del db
