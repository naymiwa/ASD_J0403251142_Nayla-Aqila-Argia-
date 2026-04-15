#Nayla Aqila Argia J04032511142
#Latihan 3: membuat traversal preorder

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder: root ==> left ==> right
def preorder(node):
    if node is not None: #cek apakah node ada
        print(node.data, end=" ") #cetak data node
        preorder(node.left) #rekursif ke kiri
        preorder(node.right) #rekursif ke kanan

#membuat tree
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi traversal preorder
print("Hasil traversal preorder:")
preorder(root)

#PENJELASAN
#Traversal preorder mengunjungi node dengan urutan root-kiri-kanan
#Fungsi preorder menggunakan rekursi untuk menelusuri tree
#Pertama mencetak root(A), lalu ke subtree kiri(B, D, E), kemudian subtree kanan(C)
#Struktur tree: A sebagai root, B dan C level 1, D dan E anak dari B
#Hasil traversal preorder: A B D E C