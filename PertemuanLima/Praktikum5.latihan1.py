####################################################################
# Nama File : praktikum5-latihan1.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Latihan 1: Rekursi Pangkat

def pangkat(a, n):
    # Base case:
    # Jika pangkat 0, hasil selalu 1
    if n == 0:
        return 1

    # Recursive case:
    # a dikalikan dengan hasil pangkat sebelumnya
    return a * pangkat(a, n - 1)


print(pangkat(2, 4))  # Output: 16


#Penjelasan Alur:
#- Fungsi memanggil dirinya sendiri hingga n = 0
#- Setelah base case tercapai, hasil dikembalikan bertahap
