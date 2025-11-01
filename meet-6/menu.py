class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.tersedia = True
    
    def pesan(self):
        if self.tersedia:
            print(f'Menu "{self.nama}" telah dipesan.')
        else:
            print(f'Maaf, menu "{self.nama}" tidak tersedia.')

    def habis(self):
        if self.tersedia:
            self.tersedia = False
            print(f'Menu "{self.nama}" sekarang habis.')
        else:
            print(f'Menu "{self.nama}" sudah tidak tersedia.')