####################################################################
# Nama File : praktikum5-materi4.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Materi 4: Konsep Dasar Backtracking
# Backtracking bekerja dengan pola:
# Choose -> Explore -> Unchoose (mundur jika selesai)

def biner(n, hasil=""):
    # Base case:
    # Jika panjang hasil sudah sama dengan n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore:
    # Tambahkan '0'
    biner(n, hasil + "0")

    # Choose + Explore:
    # Tambahkan '1'
    biner(n, hasil + "1")


# Pemanggilan fungsi
# Akan menghasilkan semua kombinasi biner sepanjang 3 digit
biner(3)


#Penjelasan Alur Program:
#- Fungsi akan terus memanggil dirinya sendiri
#- Setiap pemanggilan menambah karakter '0' atau '1'
#- Jika panjang string sudah n, fungsi berhenti (base case)
#- Jumlah kombinasi = 2^n