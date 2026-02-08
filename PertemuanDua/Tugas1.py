#====================
# Tugas 1 : ADT dan File Handling
# Studi Kasus : Data Barang / Stok Barang
#====================

nama_file = "data_barang.txt"


#====================
# Fungsi load data barang
#====================

def baca_data_barang(nama_file):
    data_dict = {}

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            parts = baris.split(',')

            if len(parts) != 3:
                continue

            kode, nama, stok_str = parts

            try:
                stok_int = int(stok_str)
            except ValueError:
                continue

            data_dict[kode] = {
                "nama": nama,
                "stok": stok_int
            }

    return data_dict


#====================
# Fungsi menampilkan data barang
#====================

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data barang kosong")
        return

    print("\n=== Daftar Barang ===")
    print(f"{'Kode':<8} | {'Nama Barang':<15} | {'Stok':>5}")
    print("-" * 35)

    for kode in sorted(data_dict):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:<8} | {nama:<15} | {stok:>5}")


#====================
# Fungsi mencari barang
#====================

def cari_barang(data_dict):
    kode_cari = input("Masukkan kode barang: ").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]["stok"]

        print("\n=== Barang Ditemukan ===")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("Barang tidak ditemukan")


#====================
# Fungsi update stok barang
#====================

def update_stok(data_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in data_dict:
        print("Kode barang tidak ditemukan")
        return

    try:
        stok_baru = int(input("Masukkan stok baru: "))
    except ValueError:
        print("Stok harus berupa angka")
        return

    if stok_baru < 0:
        print("Stok tidak boleh negatif")
        return

    stok_lama = data_dict[kode]["stok"]
    data_dict[kode]["stok"] = stok_baru

    print(f"Stok berhasil diupdate dari {stok_lama} menjadi {stok_baru}")


#====================
# Fungsi tambah barang baru
#====================

def tambah_barang(data_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in data_dict:
        print("Kode barang sudah ada! Tidak boleh duplikat.")
        return

    nama = input("Masukkan nama barang: ").strip()

    if nama == "":
        print("Nama barang tidak boleh kosong")
        return

    try:
        stok = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka")
        return

    if stok < 0:
        print("Stok tidak boleh negatif")
        return

    data_dict[kode] = {
        "nama": nama,
        "stok": stok
    }

    print("Barang baru berhasil ditambahkan!")


#====================
# Fungsi simpan data ke file
#====================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")


#====================
# Fungsi main & menu
#====================

def main():
    data_barang = baca_data_barang(nama_file)

    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Update stok barang")
        print("4. Tambah barang baru")
        print("5. Simpan data")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(data_barang)

        elif pilihan == "2":
            cari_barang(data_barang)

        elif pilihan == "3":
            update_stok(data_barang)

        elif pilihan == "4":
            tambah_barang(data_barang)

        elif pilihan == "5":
            simpan_data(nama_file, data_barang)
            print("Data barang berhasil disimpan!")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid")


#====================
# Program utama
#====================

if __name__ == "__main__":
    main()
