# Praktikum 11 - Latihan 1 (BFS)
# Nama: Nayla Aqila Argia
# NIM: J0403251142

from collections import deque

# Graph lokasi
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # langsung isi awal

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')


# Jawaban Pertanyaan:
# 1. Node pertama: Rumah
#    karena BFS selalu mulai dari node awal
#
# 2. BFS cocok untuk jalur terdekat karena:
#    BFS mengecek semua node per level
#    sehingga jalur pertama yang ditemukan adalah yang paling pendek
#
# 3. Jika struktur graph berubah:
#    urutan BFS juga berubah karena tetangga yang dikunjungi berbeda