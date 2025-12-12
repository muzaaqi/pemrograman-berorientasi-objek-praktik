import sqlite3
import os
from time import sleep

conn = sqlite3.connect('sewa.db')
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS motor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                plat TEXT NOT NULL,
                harga_sewa INTEGER NOT NULL,
                status TEXT NOT NULL)""")
conn.commit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pesan(msg=""):
    clear()
    length = len(msg) + 4
    print(f"{'-' * length}\n[!] {msg}\n{'-'*length}")

def tampilkan_semua_motor():
    cursor.execute("SELECT * FROM motor")
    data = cursor.fetchall()
    if not data:
        pesan("Tidak ada motor.")
        return
    print("\nDaftar Motor:")
    print(f"{'ID':<3} | {'NAMA':<10} | {'PLAT':<14} | {'HARGA SEWA':<11} | STATUS")
    for row in data:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<14} | {row[3]:<11} | {row[4]}")

def tambah_motor(nama, plat, harga_sewa):
    cursor.execute("""
                    INSERT INTO motor (nama, plat, harga_sewa, status) 
                    VALUES (?, ?, ?, ?)
                    """, (nama, plat, harga_sewa, 'Tersedia'))
    conn.commit()
    pesan(f"Motor {nama} berhasil ditambahkan.")

def update_motor(id_motor, nama_baru, plat_baru, harga_baru):
    cursor.execute("""
                    UPDATE motor 
                    SET nama = ?, plat = ?, harga_sewa = ? 
                    WHERE id = ?
                    """, (nama_baru, plat_baru, harga_baru, id_motor))
    if cursor.rowcount == 0:
        pesan("ID motor tidak ditemukan.")
        return
    conn.commit()
    pesan(f"Motor dengan ID {id_motor} berhasil diperbarui.")

def hapus_motor(id_motor):
    cursor.execute("DELETE FROM motor WHERE id = ?", (id_motor,))
    cursor.rowcount
    if cursor.rowcount == 0:
        pesan("ID motor tidak ditemukan.")
        return
    conn.commit()
    pesan(f"Motor dengan ID {id_motor} berhasil dihapus.")

def cari_motor(keyword):
    cursor.execute("""
                    SELECT * FROM motor 
                    WHERE nama LIKE ?
                    """, (f'%{keyword}%',))
    data = cursor.fetchall()
    if not data:
        pesan("Tidak ada data yang ditemukan.")
        return
    print("\nHasil Pencarian:")
    print(f"{'ID':<3} | {'NAMA':<10} | {'PLAT':<14} | {'HARGA SEWA':<11} | STATUS")
    for row in data:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<14} | {row[3]:<11} | {row[4]}")

def tampilkan_motor_tersdia():
    cursor.execute("""
                    SELECT * FROM motor 
                    WHERE status = 'Tersedia'
                    """)
    data = cursor.fetchall()
    if not data:
        pesan("Tidak ada motor tersedia.")
        return
    print("\nMotor Tersedia:")
    print(f"{'ID':<3} | {'NAMA':<10} | {'PLAT':<14} | {'HARGA SEWA':<11} | STATUS")
    for row in data:
        print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<14} | {row[3]:<11} | {row[4]}")

def sewa_motor(id_motor):
    cursor.execute("""
                    UPDATE motor 
                    SET status = 'Dipinjam' 
                    WHERE id = ? AND status = 'Tersedia'
                    """, (id_motor,))
    if cursor.rowcount == 0:
        pesan("Motor tidak tersedia untuk disewa atau ID motor tidak valid.")
    else:
        conn.commit()
        pesan(f"Motor dengan ID {id_motor} berhasil disewa.")

def kembalikan_motor(id_motor, lama_sewa):
    cursor.execute("""SELECT * FROM motor WHERE id = ?""", (id_motor,))
    motor = cursor.fetchone()
    cursor.execute("""
                    UPDATE motor 
                    SET status = 'Tersedia' 
                    WHERE id = ? AND status = 'Dipinjam'
                    """, (id_motor,))
    if cursor.rowcount == 0:
        pesan("Motor tidak dalam status dipinjam atau ID motor tidak valid.")
        return
    else:
        conn.commit()
        pesan(f"Motor {motor[1]} berhasil dikembalikan.")
        total_biaya = motor[3] * lama_sewa
        print("Detail Sewa")
        print(f"Nama Motor: {motor[1]}")
        print(f"Plat Motor: {motor[2]}")
        print(f"Lama Sewa: {lama_sewa} hari")
        print(f"Total Biaya: Rp {total_biaya}")


def menu():
    while True:
        print("\n=== SEWA MOTOR “KELAS I JAYA JAYA” ===")
        print("[1] Tampilkan Semua Motor")
        print("[2] Tambah Motor")
        print("[3] Update Motor")
        print("[4] Hapus Motor")
        print("[5] Cari Motor")
        print("[6] Tampilkan Motor Tersedia")
        print("[7] Sewa Motor")
        print("[8] Kembalikan Motor")
        print("[9] Keluar")
        
        pilihan_menu = input("Pilih menu (1-9): ")
        if pilihan_menu == '1':
            clear()
            tampilkan_semua_motor()
        elif pilihan_menu == '2':
            clear()
            nama = input("Masukkan nama motor: ")
            plat = input("Masukkan plat motor: ")
            harga_sewa = int(input("Masukkan harga sewa: "))
            tambah_motor(nama, plat, harga_sewa)
        elif pilihan_menu == '3':
            clear()
            id_motor = int(input("Masukkan ID motor yang akan diupdate: "))
            nama_baru = input("Masukkan nama baru: ")
            plat_baru = input("Masukkan plat baru: ")
            harga_baru = int(input("Masukkan harga sewa baru: "))
            update_motor(id_motor, nama_baru, plat_baru, harga_baru)
        elif pilihan_menu == '4':
            clear()
            id_motor = int(input("Masukkan ID motor yang akan dihapus: "))
            hapus_motor(id_motor)
        elif pilihan_menu == '5':
            clear()
            keyword = input("Masukkan kata kunci pencarian: ")
            cari_motor(keyword)
        elif pilihan_menu == '6':
            clear()
            tampilkan_motor_tersdia()
        elif pilihan_menu == '7':
            clear()
            id_motor = int(input("Masukkan ID motor yang akan disewa: "))
            sewa_motor(id_motor)
        elif pilihan_menu == '8':
            clear()
            id_motor = int(input("Masukkan ID motor yang akan dikembalikan: "))
            lama_sewa = int(input("Masukkan lama sewa (dalam hari): "))
            kembalikan_motor(id_motor, lama_sewa)
        elif pilihan_menu == '9':
            pesan("Terima kasih...")
            sleep(2)
            clear()
            break

menu()
conn.close()