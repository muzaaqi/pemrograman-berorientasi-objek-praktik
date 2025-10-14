class Stopword:
    def __init__(self, id, stopword):
        self.id = id
        self.stopword = stopword

    def tambah_stopword(self, kata):
        self.stopword = kata

    def tampil_data(self):
        return f"{self.id}. {self.stopword}"

    def update_data(self, new_word):
        self.stopword = new_word

    def hapus(self):
        del self.stopword


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_user(self):
        return {"id": self.id, "username": self.username}

    def process_edit(self, username=None, password=None):
        if username:
            self.username = username
        if password:
            self.password = password

    def create_user(self, id, username, password):
        return User(id, username, password)

    def delete_user(self):
        del self.username
        del self.password


class Mapel:
    def __init__(self, id, mata_pelajaran):
        self.id = id
        self.mata_pelajaran = mata_pelajaran

    def tambah_mapel(self, nama):
        self.mata_pelajaran = nama

    def tampil_data(self):
        return f"[{self.id}] {self.mata_pelajaran}"

    def update_data(self, nama_baru):
        self.mata_pelajaran = nama_baru

    def hapus(self):
        del self.mata_pelajaran


class Jadwal:
    def __init__(self, id, id_mapel, waktu):
        self.id = id
        self.id_mapel = id_mapel
        self.waktu = waktu

    def tambah_jadwal(self, waktu):
        self.waktu = waktu

    def tampil_data(self):
        return f"Mapel dengan ID {self.id_mapel} dijadwalkan pada {self.waktu}"

    def update_data(self, waktu_baru):
        self.waktu = waktu_baru

    def hapus(self):
        del self.waktu


class Biaya:
    def __init__(self, id, id_mapel, biaya):
        self.id = id
        self.id_mapel = id_mapel
        self.biaya = biaya

    def tampil_data(self):
        return f"Biaya untuk mapel dengan ID {self.id_mapel}: Rp {self.biaya}"

    def update_data(self, biaya_baru):
        self.biaya = biaya_baru

    def delete(self):
        del self.biaya

    def tambah_biaya(self, biaya):
        self.biaya = biaya


class Pertanyaan:
    def __init__(self, id, mata_pelajaran, pertanyaan):
        self.id = id
        self.mata_pelajaran = mata_pelajaran
        self.pertanyaan = pertanyaan

    def tambah_pertanyaan(self, pertanyaan):
        self.pertanyaan = pertanyaan

    def tampil_data(self):
        return f"[{self.mata_pelajaran}] {self.pertanyaan}"

    def hapus(self):
        del self.pertanyaan


# === Contoh Implementasi ===
if __name__ == "__main__":
    user1 = User(1, "admin", "1234")
    mapel1 = Mapel(1, "Bahasa Inggris")
    jadwal1 = Jadwal(1, mapel1.id, "Senin 09:00")
    biaya1 = Biaya(1, mapel1.id, "500000")

    print(user1.get_user())
    print(mapel1.tampil_data())
    print(jadwal1.tampil_data())
    print(biaya1.tampil_data())
