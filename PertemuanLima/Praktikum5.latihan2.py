####################################################################
# Nama File : praktikum5-latihan2.py
# Nama      : Nayla Aqila Argia
# NIM       : J0403251142
# Kelas     : B2
####################################################################

# Latihan 2: Tracing Rekursi

def countdown(n):
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)


countdown(3)


#Diskusi:
#- Output 'Masuk' muncul dari 3 ke 1
#- Output 'Keluar' muncul terbalik (1 ke 3)
#- Hal ini terjadi karena konsep call stack (LIFO)
