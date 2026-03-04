##################################
# Nama: Nayla Aqila Argia
# NIM: J0403251142
##################################

#Latihan 1

def insertion_sort(data):

    for i in range(1, len(data)):

        key = data[i]  
        #menyimpan nilai yang akan dipindahkan ke posisi yang benar

        j = i - 1  
        #j menunjuk elemen terakhir di bagian kiri

        while j >= 0 and data[j] > key:
        #selama belum melewati awal list dan elemen kiri lebih besar dari key

            data[j + 1] = data[j]
            #geser elemen yang lebih besar satu langkah ke kanan

            j -= 1
            #mundur satu posisi ke kiri untuk cek elemen berikutnya

        #Menyisipkan key ke posisi yang tepat
        data[j + 1] = key
        #menempatkan key setelah semua pergeseran selesai

    return data


data = [7, 8, 5, 2, 4, 6]
print("Hasil Sorting:", insertion_sort(data))

#1. Perulangan dimulai dari indeks 1 karena elemen pertama (index 0) dianggap sudah terurut
#2. key adalah nilai yang akan disisipkan ke posisi yang benar pada bagian kiri
#3. Menggunakan while karena jumlah pergeseran tidak pasti (tergantung kondisi)
#4. Menggeser elemen yang lebih besar ke kanan