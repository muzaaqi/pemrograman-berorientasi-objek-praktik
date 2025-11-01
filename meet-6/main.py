class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False
    
    def pinjam(self):
        if not self.dipinjam:
            self.dipinjam = True
            print(f'Buku "{self.judul}" telah dipinjam.')
        else:
            print(f'Buku "{self.judul}" sedang dipinjam.')
    
    def kembalikan(self):
        if self.dipinjam:
            self.dipinjam = False
            print(f'Buku "{self.judul}" telah dikembalikan.')
        else:
            print(f'Buku "{self.judul}" belum dipinjam.')