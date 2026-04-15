#Nayla Aqila Argia J04032511142
#Latihan 2: membuat Node

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

#menampilkan isi node
print("Data pada root:", root.data)
print("Data child kiri root:", root.left.data)
print("Data child kanan root:", root.right.data)
print("Data child kiri dari B:", root.left.left.data)
print("Data child kanan dari B:", root.left.right.data)
print("Data child kiri dari C:", root.right.left.data)
print("Data child kanan dari C:", root.right.right.data)

#PENJELASAN
#Class Node digunakan untuk membangun struktur Binary Tree
#Setiap node memiliki data, child kiri (left), dan child kanan (right)
#Root adalah node utama yaitu A
#Level 1 berisi B dan C sebagai anak dari root
#Level 2 berisi D, E (anak dari B) dan F, G (anak dari C)
#Relasi antar node dibuat dengan menghubungkan atribut left dan right
#Output menampilkan isi tiap node menggunakan akses bertingkat seperti root.left.right