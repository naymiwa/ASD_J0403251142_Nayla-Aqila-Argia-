# ==========================================================
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Latihan 6: Rotasi Kanan
# ==========================================================

# Class Node
# Fungsi: Membuat node pada BST yang berisi data dan pointer ke left & right
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# Fungsi rotate_right
# Alur:
# 1. Ambil child kiri (x)
# 2. Simpan subtree kanan x (T2)
# 3. Rotasi:
#    - x jadi root baru
#    - y jadi kanan dari x
def rotate_right(y):
    x = y.left
    T2 = x.right

    # proses rotasi
    x.right = y
    y.left = T2

    return x


# tree tidak seimbang (condong kiri)
root = Node(30) # node paling atas
root.left = Node(20)
root.left.left = Node(10) #dibawah node 20

print("Sebelum rotasi:")
tampil_struktur(root) # print struktutr 

# rotasi kanan
root = rotate_right(root)

print("\nSesudah rotasi:")
tampil_struktur(root)