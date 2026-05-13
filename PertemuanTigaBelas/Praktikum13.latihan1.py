# Nama : Nayla Aqila Argia
# NIM : J0403251142
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph awal
print("Edge pada graph:")

for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# 1. Graph awal memiliki lebih banyak edge dan dapat
#    membentuk cycle, sedangkan spanning tree hanya
#    memiliki edge yang diperlukan untuk menghubungkan
#    semua node tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena
#    cycle menyebabkan penggunaan edge berlebih dan
#    membuat graph menjadi tidak efisien.
# 3. Jumlah edge spanning tree lebih sedikit karena
#    spanning tree hanya membutuhkan n-1 edge untuk
#    menghubungkan seluruh node.