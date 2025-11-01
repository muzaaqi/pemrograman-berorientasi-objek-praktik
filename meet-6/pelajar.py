class Pleajar:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan

    def perkenalan(self):
        print(f'Halo, nama saya {self.nama}, NPM saya {self.npm} dan saya jurusan {self.jurusan}.')
    
    def ubah_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru
        print(f'Jurusan saya telah diubah menjadi {self.jurusan}.')
        
        
        
