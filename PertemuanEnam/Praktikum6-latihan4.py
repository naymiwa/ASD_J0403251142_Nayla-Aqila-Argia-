##################################
# Nama: Nayla Aqila Argia
# NIM: J0403251142
##################################

#Latihan 4

def merge_sort(data):

    if len(data) <= 1:
        return data

    #Membagi list menjadi dua bagian
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    #Fungsi memanggil dirinya sendiri
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    #Menggabungkan kembali
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = [] #array kosong
    i = 0
    j = 0

    #Menggabungkan dua list yang sudah terurut
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


data = [5, 2, 4, 6, 1, 3]
print("Hasil Sorting:", merge_sort(data))

#1. base case adalah kasus pada rekursif dimana kode akan berhenti dan menghasilkan output yang sudah dibuat
#2. fungsi memanggil dirinya sendiri untuk mempersingkat kode (rekursif)
#3. untuk menggabungkan dua list menjadi satu list terurut
