# Implementasi BFS
# Nama: Nayla Aqila Argia
# NIM: J0403251142

from collections import deque   # import deque untuk antrian (queue)

# Representasi graph dalam bentuk adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph menggunakan BFS

    queue = deque()   # queue untuk menyimpan node yang akan diproses
    visited = set()   # set untuk menyimpan node yang sudah dikunjungi

    queue.append(start)   # masukkan node awal ke queue
    visited.add(start)    # tandai node awal sudah dikunjungi

    while queue:   # selama queue tidak kosong
        node = queue.popleft()   # ambil node paling depan (FIFO)
        print(node, end=' ')     # tampilkan node

        # cek semua tetangga dari node saat ini
        for neighbor in graph[node]:
            if neighbor not in visited:   # jika belum dikunjungi
                visited.add(neighbor)     # tandai sebagai sudah dikunjungi
                queue.append(neighbor)   # masukkan ke queue untuk diproses nanti

# Menjalankan BFS dari node A
bfs(graph, 'A')