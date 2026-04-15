#Nayla Aqila Argia J04032511142
#Latihan 4: membuat traversal inorder

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi inorder: left > root > right
def inorder(node):
    if node is not None: #cek apakah node ada
        inorder(node.left) #rekursif ke kiri
        print(node.data, end=" ") #cetak data node
        inorder(node.right) #rekursif ke kanan

#membuat tree
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi traversal inorder
print("Hasil traversal inorder:")
inorder(root)

#PENJELASAN
#Traversal inorder mengunjungi node dengan urutan kiri-root-kanan
#Fungsi menggunakan rekursi untuk menelusuri subtree kiri, lalu root, lalu subtree kanan
#Struktur tree: A sebagai root, B dan C level 1, D dan E anak dari B
#Urutan hasil inorder: D B E A C