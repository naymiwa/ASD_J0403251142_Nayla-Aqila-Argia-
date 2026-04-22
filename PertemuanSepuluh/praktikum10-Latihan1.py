# ==========================================================
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Praktikum 10 - Latihan 1-3 (BST)
# ==========================================================

# Class Node
# Fungsi: Membuat node pada BST yang berisi data dan pointer ke left & right
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai node
        self.left = None      # pointer ke child kiri
        self.right = None     # pointer ke child kanan

# Fungsi insert
# Alur:
# 1. Jika root kosong → buat node baru
# 2. Jika data < root → masuk ke kiri
# 3. Jika data > root → masuk ke kanan
# 4. Menggunakan rekursi sampai menemukan posisi kosong
def insert(root, data):
    if root is None:
        return Node(data)  # membuat node baru jika kosong

    if data < root.data:
        root.left = insert(root.left, data)   # rekursi ke kiri
    elif data > root.data:
        root.right = insert(root.right, data) # rekursi ke kanan

    return root

# Fungsi inorder
# Alur:
# 1. Kunjungi kiri
# 2. Cetak root
# 3. Kunjungi kanan
# Hasil: data akan terurut(sorting)
def inorder(root):
    if root is not None:
        inorder(root.left)          # ke kiri dulu
        print(root.data, end=" ")   # tampilkan data
        inorder(root.right)         # ke kanan

# Fungsi search
# Alur:
# 1. Jika root kosong → tidak ditemukan
# 2. Jika sama → ditemukan
# 3. Jika lebih kecil → cari ke kiri
# 4. Jika lebih besar → cari ke kanan
def search(root, key):
    if root is None:
        return False   # data tidak ditemukan

    if root.data == key:
        return True    # data ditemukan

    elif key < root.data:
        return search(root.left, key)   # cari ke kiri
    else:
        return search(root.right, key)  # cari ke kanan
    
# program utama
root = None

data_list = [50, 30, 70, 20, 40, 60, 80]

# proses insert semua data ke BST
for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

# traversal inorder
print("Hasil inorder:")
inorder(root)

# uji search
key = 10

print("\n\nHasil pencarian:")
if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")