# Nama : Nayla Aqila Argia
# NIM : J0403251142
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Node awal dimasukkan ke visited
    visited = set([start])

    # Priority queue edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Selama masih ada edge
    while edges:

        # Mengambil edge terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Memanggil fungsi Prim
mst, total = prim(graph, 'A')

# Menampilkan hasil
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)



# 1. Node awal yang digunakan adalah A.
# 2. Edge yang dipilih pertama kali adalah A-C
#    dengan bobot 2.
# 3. Prim menentukan edge berikutnya dengan memilih
#    edge terkecil yang terhubung dengan node yang
#    sudah dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Perbedaan Prim dan Kruskal adalah:
#    - Prim membangun tree dari satu node awal.
#    - Kruskal memilih edge terkecil secara global.
