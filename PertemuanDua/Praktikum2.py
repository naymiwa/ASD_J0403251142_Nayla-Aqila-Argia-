#====================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1 : Membuat fungsi load data
#====================

nama_file = "PertemuanDua/data_mahasiswa.txt"

# membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {}  # inisialisasi buat variabel untuk dictionary

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # Hilangkan newline
            parts = baris.split(',')

            # validasi format data
            if len(parts) != 3:
                continue

            nim, nama, nilai_str = parts

            try:
                nilai_int = int(nilai_str)
            except ValueError:
                continue

            # Simpan ke dictionary
            data_dict[nim] = {
                "nama": nama,
                "nilai": nilai_int
            }

    return data_dict


#====================
# Latihan 2 : Fungsi menampilkan data
#====================

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data kosong")
        return

    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)

    for nim in sorted(data_dict):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")


#====================
# Latihan 3 : Fungsi mencari data
#====================

def cari_data(data_dict):
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n=== Data Ditemukan ===")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData tidak ditemukan")


#====================
# Latihan 4 : Fungsi update nilai
#====================

def update_nilai(data_dict):
    nim = input("Masukkan NIM yang ingin diupdate: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 - 100")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil! Nilai {nim} dari {nilai_lama} menjadi {nilai_baru}")


#====================
# Latihan 5 : Fungsi simpan data ke file
#====================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")


#====================
# Latihan 6 : Fungsi main & menu
#====================

def main():
    # load data dari file
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            update_nilai(buka_data)

        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan ke file!")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


#====================
# Program utama
#====================

if __name__ == "__main__":
    main()
