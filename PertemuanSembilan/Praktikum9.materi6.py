#Nama:Nayla Aqila Argia
#NIM:J04032511142
#Latihan 6: membuat traversal preorder

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder: root > left > right
def preorder(node):
    if node is not None: #cek apakah node ada
        print(node.data, end=" ") #cetak data (root)
        preorder(node.left) #rekursif ke kiri
        preorder(node.right) #rekursif ke kanan

#membuat tree struktur organisasi
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.left = Node("Staff 3")

#menampilkan hasil traversal
print("Struktur organisasi (preorder):")
preorder(root)

#PENJELASAN
#Tree digunakan untuk merepresentasikan struktur organisasi
#Direktur sebagai root, Manajer A dan B sebagai level 1
#Staff 1,2 di bawah Manajer A dan Staff 3 di bawah Manajer B
#Fungsi preorder mencetak data dengan urutan root-kiri-kanan
#Sehingga urutan output: Direktur Manajer A Staff 1 Staff 2 Manajer B Staff 3
#Print(root) tidak menampilkan isi karena hanya mencetak objek, bukan datanya