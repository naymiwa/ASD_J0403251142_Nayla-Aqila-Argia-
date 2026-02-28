####################################
# Nama file: praktikum5-materi1.py
# Nama: Nayla Aqila Argia       
# NIM: J0403251142
# Kelas: B2
####################################

#Materi: Rekursif
#Base case: kondisi dimana fungsi rekursif berhenti memanggil dirinya sendiri
#Recursive case: kondisi dimana fungsi rekursif memanggil dirinya sendiri

#Faktorial: n! = n * (n-1)! dengan 0! = 1
def faktorial(n):
    if n == 0: #base case
        return 1
    else: #recursive case
        return n * faktorial(n-1)
    
n = input("Masukkan nilai n untuk menghitung faktorial: ")
print(f"Faktorial dari {n} adalah {faktorial(int(n))}") 