# Nama : Nayla Aqila Argia
# NIM : J0403251142
# Kelas : B2

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []  # Menyimpan hasil MST
total_weight = 0  # Menyimpan total bobot MST

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Proses memilih edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        # Menambahkan node ke set connected
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)