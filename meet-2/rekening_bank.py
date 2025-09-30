class RekeningBank:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def lihat_saldo(self):
        return self.saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            return f"Berhasil setor: {jumlah}. Saldo sekarang: {self.saldo}"
        else:
            return "Jumlah setor harus positif."