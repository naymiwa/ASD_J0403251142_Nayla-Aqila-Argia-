##################################
# Nama: Nayla Aqila Argia
# NIM: J0403251142
##################################

# Insertion Sort dgn tracing

def insertion_sort(data):
    
    #melihat data awal
    print("Data awal: ", data)
    print("="*50)
        
    #loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yg disisipkan
        j = i-1 #index elemen terakhir di bagian kiri
        print("iterasi ke-", i)
        print("nilai key=", key)
        print("bagian kiri (terurut): ", data[:i])
        print("bagian kanan (blm terurut): ", data[i:])
        
        #geser 
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi
        data[j+1] = key
        
        print("setelah disisipkan :", data)
        print("-"*50)
    return data

angka= [7,8,5,2,4,6]
print("Hasil sorting: ", insertion_sort(angka))


            
        