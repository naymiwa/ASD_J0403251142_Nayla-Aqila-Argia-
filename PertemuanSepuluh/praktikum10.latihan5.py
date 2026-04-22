# ==========================================================
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Latihan 5: Rotasi Kiri
# ==========================================================

# Class Node
# Fungsi: Membuat node pada BST yang berisi data dan pointer ke left & right
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# preorder traversal
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# tampil struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotate_left
# Alur:
# 1. Ambil child kanan (y)
# 2. Simpan subtree kiri y (T2)
# 3. Rotasi:
#    - y jadi root baru
#    - x jadi kiri dari y
def rotate_left(x):
    y = x.right
    T2 = y.left

    # proses rotasi
    y.left = x
    x.right = T2

    return y


# membuat tree tidak seimbang
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Sebelum rotasi:")
tampil_struktur(root)

# rotasi kiri
root = rotate_left(root)

print("\nSesudah rotasi:")
tampil_struktur(root)