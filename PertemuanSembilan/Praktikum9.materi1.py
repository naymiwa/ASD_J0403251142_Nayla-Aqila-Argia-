# Nayla Aqila Argia J04032511142
# Latihan 1: Membuat Node (dasar Binary Tree)

class Node:
    def __init__(self, data):
        self.data = data      #menyimpan nilai node
        self.left = None      #child kiri
        self.right = None     #child kanan


#membuat root (node pertama)
root = Node("A")

#menampilkan isi node
print("Data pada root:", root.data)
print("Data child kiri root:", root.left)
print("Data child kanan root:", root.right)


#penjelasan
#Class Node digunakan sebagai struktur dasar Binary Tree.
#Setiap node memiliki:
#- data  : nilai yang disimpan
#- left  : pointer ke anak kiri
#- right : pointer ke anak kanan
#Pada kode ini: - Kita membuat satu node dengan nilai "A" sebagai root. Karena belum ada child, maka left dan right bernilai None