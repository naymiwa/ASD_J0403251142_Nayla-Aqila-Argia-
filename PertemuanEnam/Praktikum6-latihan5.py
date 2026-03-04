##################################
# Nama: Nayla Aqila Argia
# NIM: J0403251142
##################################

#Latihan 5

def merge(left, right):

    result = []  #menampung hasil penggabungan
    i = 0  #pointer untuk left
    j = 0  #pointer untuk right

    while i < len(left) and j < len(right):
        #selama kedua list masih punya elemen

        #kondisi agar ascending
        if left[i] <= right[j]:  #bandingkan elemen terkecil
            result.append(left[i])  #ambil dari left
            i += 1  #maju pointer left
        else:
            result.append(right[j])  #ambil dari right
            j += 1  #maju pointer right

    result.extend(left[i:])  #tambah sisa left jika ada
    result.extend(right[j:])  #tambah sisa right jika ada

    return result  #kembalikan hasil merge


left = [1, 4, 6]
right = [2, 3, 5]

print("Hasil Merge:", merge(left, right))

#1. left[i] <= right[j]:
#2. result.extend() berfungsi untuk menambahkan sisa elemen yang belum diproses