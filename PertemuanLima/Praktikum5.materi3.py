#Materi rekursif: menjumlahkan elemen list

def jumlah_list(data, index=0):
    #base case:
    if index == len(data):
        return 0
    #recursive case: jika index masih dalam batas list
    return data[index] + jumlah_list(data, index+1)

print("===Program jumlah data list===")
print(jumlah_list([2,4,5,6,8]))