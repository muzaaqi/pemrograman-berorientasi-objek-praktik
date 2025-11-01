class Anjing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def menggonggong(self):
        return f'{self.nama} sedang menggonggong.'

    def info(self):
        return f'Anjing {self.nama} berumur {self.umur} tahun.'