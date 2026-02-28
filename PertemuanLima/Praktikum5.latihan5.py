####################################################################
# Nama File : praktikum5-latihan5.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Studi Kasus: Generator PIN 3 Digit

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


buat_pin(3)
