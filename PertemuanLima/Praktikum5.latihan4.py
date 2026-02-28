####################################################################
# Nama File : praktikum5-latihan4.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Latihan 4: Kombinasi Huruf A dan B

def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return

    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


kombinasi(2)


#Diskusi:
#- Setiap posisi memiliki 2 pilihan (A atau B)
#- Jumlah kombinasi = 2^n
