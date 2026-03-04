##################################
# Nama: Nayla Aqila Argia
# NIM: J0403251142
##################################

#Latihan 2

def insertion_sort(data):
    for i in range(1, len(data)):  #mulai dari elemen kedua
        key = data[i]  #nilai yang akan disisipkan
        j = i -1  #indeks elemen kiri
        
        while j >= 0 and data[j] > key:  #selama elemen kiri lebih besar
            data[j + 1] = data[j]  #geser ke kanan
            j -= 1  #mundur ke kiri

        data[j + 1] = key  #tempatkan key di posisi benar

    return data

angka = [5,2,4,6,1,3]
print(insertion_sort(angka))

#1. ascending = data[j] > key
#2. descending = data[j] < key