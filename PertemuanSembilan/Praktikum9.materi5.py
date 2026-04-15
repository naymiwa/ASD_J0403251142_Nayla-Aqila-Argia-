#Nayla Aqila Argia J04032511142
#Latihan 5: membuat traversal postorder

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi postorder: left > right > root
def postorder(node):
    if node is not None: #cek apakah node ada
        postorder(node.left) #rekursif ke kiri
        postorder(node.right) #rekursif ke kanan
        print(node.data, end=" ") #cetak data node

#membuat tree
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi traversal postorder
print("Hasil traversal postorder:")
postorder(root)

#PENJELASAN
#Traversal postorder mengunjungi node dengan urutan kiri-kanan-root
#Fungsi menggunakan rekursi: selesaikan subtree kiri, lalu subtree kanan, terakhir root
#Struktur tree: A sebagai root, B dan C level 1, D dan E anak dari B
#Urutan hasil postorder: D E B C A