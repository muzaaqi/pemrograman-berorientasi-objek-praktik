class BankAccount:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self._saldo = saldo_awal
        self.__nomor_rekening = "123456789"

    def get_saldo(self):
        return self._saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            print(f"Menyetor: {jumlah}. Saldo baru adalah {self._saldo}")
        else:
            print("Jumlah setoran tidak valid.")
    
    def tarik(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah
            print(f"Menarik: {jumlah}. Saldo baru adalah {self._saldo}")
        else:
            print("Jumlah penarikan tidak valid")
    
    def _periksa_status_rekening(self):
        return self._saldo > 0
    
    def __get_nomor_rekening(self):
        return self.__nomor_rekening
    
    def tampilkan_info_rekening(self):
        print(f"Pemilik: {self.pemilik}")
        print(f"Saldo: {self._saldo}")
        print(f"Nomor Rekening: {self.__get_nomor_rekening()}")


rekening = BankAccount("Alice", 1000)
    
print(f"Pemilik Rekening: {rekening.pemilik}")
print(f"Saldo Awal: {rekening.get_saldo()}")
rekening.setor(500)
rekening.tarik(200)

print(f"Saldo Protected: {rekening._saldo}")
print(f"Status Rekening: {rekening._periksa_status_rekening()}")

try:
    print(rekening.__nomor_rekening)
except AttributeError as e:
    print(e)

try:
    print(rekening.__get_nomor_rekening())
except AttributeError as e:
    print(e)

print(f"Nomor Rekening Private: {rekening._BankAccount__nomor_rekening}")
print(f"Nomor Rekening Private (method): {rekening._BankAccount__get_nomor_rekening()}")

rekening.tampilkan_info_rekening()
rekening.__get_nomor_rekening()