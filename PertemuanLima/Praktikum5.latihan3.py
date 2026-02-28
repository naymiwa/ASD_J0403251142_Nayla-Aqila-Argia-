####################################################################
# Nama File : praktikum5-latihan3.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Latihan 3: Mencari Nilai Maksimum

def cari_maks(data, index=0):
    # Base case:
    # Jika index berada di elemen terakhir
    if index == len(data) - 1:
        return data[index]

    # Recursive case:
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


#Penjelasan:
#- Fungsi membandingkan elemen saat ini dengan elemen berikutnya
#- Proses berjalan hingga elemen terakhir
