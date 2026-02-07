#====================
# Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1: Membaca seluruh isi file
#====================

#Membuka file dengan mode read('r')

#Membuka file dalam satu string
print()
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file: #file=variabel
    isi_file = file.read() #Membaca keseluruhan isi file dalam satu string
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah baris", isi_file.count("\n")+1)

#Membuka file per baris
print("===Membaca File per Baris===")
jumlah_baris=0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
   for baris in file:
       jumlah_baris= jumlah_baris + 1
       baris = baris.strip() #menghilangkan baris baru \n (ambil data murni)
       print("Baris ke-", jumlah_baris)
       print("Isinya :", baris)

#====================
# Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Parsing baris menjadi kolom data
#====================
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file: #buka file per baris pakai looping
        baris = baris.strip() #Hilangkan Newline (\n)
        nim, nama, nilai = baris.split(",") #Parsing, Pemisahan berdasarkan koma 
        print("NIM :", nim, "| Nama : ", nama, "| Nilai : ", int(nilai))

#====================
# Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca File dan Menyimpan ke List
#====================

data_list = [] #Buat List untuk menampung data mahasiswa
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Hilangkan Newline

        nim,nama, nilai = baris.split(',')

        #Simpan sebagai list " [nim,nama, nilai] "
        data_list.append([nim,nama,int(nilai)]) #Mengisi/nyimpan data dalam list

print("==== Data Mahasiswa dalam LIST ====")
print(data_list)

print("==== Jumlah Record dalam LIST ====")
print("Jumlah Record: ", len(data_list))

print("==== Menampilkan Data Record Tertentu ====")
print("Contoh Record Pertama:  ", data_list[0]) #

#====================
# Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary
#====================

data_dict ={} #buat variabel untuk dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Hilangkan Newline

        nim, nama, nilai = baris.split(',')

        #Simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim]= { #Key
            "nama": nama, #Values
            "nilai": int(nilai) #Values
        }
print("=== Data Mahasiswa dalam Dictionary ===")
print(data_dict)