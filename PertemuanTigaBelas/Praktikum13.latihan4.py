# Nama : Nayla Aqila Argia
# NIM : J0403251142
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Studi Kasus: Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal
# ==========================================================

# Daftar edge graph
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()

mst = []
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)


# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih:
#    - GedungC - GedungD = 1
#    - GedungA - GedungC = 2
#    - GedungB - GedungD = 3
# 3. Total biaya minimum adalah 6.
# 4. MST cocok digunakan karena dapat menghubungkan
#    seluruh gedung dengan biaya pemasangan kabel
#    paling minimum tanpa koneksi berlebih.