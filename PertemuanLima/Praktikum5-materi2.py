#############################
# Nama: Nayla Aqila Argia
# NIM: J0403251142  
# Kelas: B2
# Materi: Rekursif
#############################

# Tracing bilangan(masuk - keluar)
#input: 3 -> #output: 3 2 1
#Masuk: 1 -2 -3
#Keluar: 3 -2 -1

def hitung(n):
    #base case
    if n == 0:
        print("selesai")
        return
    
    print("Masuk: ", n)
    hitung(n-1) #recursive case
    print("Keluar: ", n) 

print("===Program Tracing===")
hitung(3)