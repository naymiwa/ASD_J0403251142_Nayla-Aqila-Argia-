##################################
# Nama: Nayla Aqila Argia
# NIM: J0403251142
##################################

#Latihan 3

def insertion_sort(data):

    print("Data awal:", data)
    print("="*50)

    for i in range(1, len(data)):  #mulai dari elemen kedua

        key = data[i]  #nilai yang akan disisipkan
        j = i - 1  #indeks elemen kiri
        pergeseran = 0  #menghitung jumlah geser

        print("Iterasi ke-", i)

        while j >= 0 and data[j] > key:  #selama elemen kiri lebih besar
            data[j + 1] = data[j]  #geser elemen ke kanan
            j -= 1  #mundur ke kiri
            pergeseran += 1  #tambah hitungan geser

        data[j + 1] = key  #tempatkan key di posisi benar

        print("Isi list:", data)
        print("Jumlah pergeseran:", pergeseran)
        print("-"*50)

    return data


data = [5, 2, 4, 6, 1, 3]
insertion_sort(data)

#1. Setelah i = 1 → [2, 5, 4, 6, 1, 3]
#2. Setelah i = 3 → [2, 4, 5, 6, 1, 3]
#3. Pergeseran pada i = 4 terjadi sebanyak 4 kali karena nilai key = 1 lebih kecil dari semua elemen di sebelah kirinya (2, 4, 5, 6)