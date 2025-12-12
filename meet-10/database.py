import sqlite3

conn = sqlite3.connect('toko.db')
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS produk (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                harga INTEGER NOT NULL,
                stok INTEGER NOT NULL)""")
conn.commit()

def tambah_produk(nama, harga, stok):
    cursor.execute("""
                    INSERT INTO produk (nama, harga, stok) 
                    VALUES (?, ?, ?)
                    """, (nama, harga, stok))
    conn.commit()
    print("Produk berhasil ditambahkan.")

def tampilkan_produk():
    cursor.execute("SELECT * FROM produk")
    data = cursor.fetchall()
    if not data:
        print("Tidak ada data produk.")
        return
    print("\nDaftar Produk:")
    print("-" * 40)
    for row in data:
        print(f"ID: {row[0]}")
        print(f"Nama: {row[1]}")
        print(f"Harga: {row[2]}")
        print(f"Stok: {row[3]}")
        print("-" * 40)

def update_produk(id_produk, nama_baru, harga_baru, stok_baru):
    cursor.execute("""
                    UPDATE produk 
                    SET nama = ?, harga = ?, stok = ? 
                    WHERE id = ?
                    """, (nama_baru, harga_baru, stok_baru, id_produk))
    conn.commit()
    print("Produk berhasil diperbarui.")

def hapus_produk(id_produk):
    cursor.execute("DELETE FROM produk WHERE id = ?", (id_produk,))
    conn.commit()
    print("Produk berhasil dihapus.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama = input("Nama produk: ")
            harga = int(input("Harga: "))
            stok = int(input("Stok: "))
            tambah_produk(nama, harga, stok)
        elif pilihan == '2':
            tampilkan_produk()
        elif pilihan == '3':
            idp= int(input("Masukkan ID produk: "))
            nama = input("Nama baru: ")
            harga = int(input("Harga baru: "))
            stok = int(input("Stok baru: "))
            update_produk(idp, nama, harga, stok)
        elif pilihan == '4':
            idp = int(input("Masukkan ID produk yang akan dihapus: "))
            hapus_produk(idp)
        elif pilihan == '5':
            print("Keluar aplikasi...")
            break
        else:
            print("Pilihan tidak valid!")

menu()

conn.close()