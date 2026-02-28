####################################################################
# Nama File : praktikum5-materi5.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Materi 5: Backtracking dengan Pruning
# Pruning digunakan untuk menghentikan pencarian yang tidak memenuhi syarat

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning:
    # Jika jumlah angka '1' melebihi batas, hentikan proses
    if jumlah_1 > batas:
        return

    # Base case:
    # Jika panjang hasil sudah mencapai n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Pilih '0' (tidak menambah jumlah_1)
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1' (jumlah_1 bertambah)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# Contoh pemanggilan
# Panjang 4 digit, maksimal 2 angka '1'
biner_batas(4, 2)


#Penjelasan:
#- Pruning mencegah eksplorasi cabang yang tidak valid
#- Program lebih efisien karena tidak mengecek semua kemungkinan