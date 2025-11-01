class Garis:
    def __init__(self, panjang):
        self.panjang = panjang

    def info(self):
        print(f'Garis dengan panjang {self.panjang} satuan.')
    
    def ubah_panjang(self, panjang_baru):
        self.panjang = panjang_baru
        print(f'Panjang garis diubah menjadi {self.panjang} satuan.')