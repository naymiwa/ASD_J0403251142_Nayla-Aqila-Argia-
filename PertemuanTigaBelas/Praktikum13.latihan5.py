# Nama : Nayla Aqila Argia
# NIM : J0403251142
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Kasus: Jaringan Jalan Antar Kota
# Menggunakan Algoritma Kruskal
# ==========================================================

# Daftar edge graph
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot minimum =", total_weight)

# 1. Kasus yang dipilih adalah Jaringan Jalan Antar Kota.
# 2. Algoritma yang digunakan adalah Kruskal.
# 3. Edge yang dipilih dalam MST:
#    - Bogor - Depok = 2
#    - Depok - Jakarta = 3
#    - Depok - Bandung = 4
# 4. Total bobot MST adalah 9.
# 5. Edge tertentu tidak dipilih karena memiliki
#    bobot lebih besar dan dapat menyebabkan cycle.