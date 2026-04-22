# ==========================================================
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Latihan 4: BST Tidak Seimbang
# ==========================================================
# Fungsi: Membuat node pada BST yang berisi data dan pointer ke left & right
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Fungsi insert BST
# Alur:
# 1. Jika root kosong → buat node baru
# 2. Jika data < root → masuk ke kiri
# 3. Jika data > root → masuk ke kanan
# 4. Menggunakan rekursi sampai menemukan posisi kosong
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Fungsi preorder
# Alur:
# Root → Left → Right
# Digunakan untuk melihat urutan struktur tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi tampil_struktur
# Alur:
# Menampilkan bentuk tree secara visual (indentasi level)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


root = None

# data urut → menyebabkan tree tidak seimbang
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

# Tree condong ke kanan → tidak seimbang → performa bisa menurun