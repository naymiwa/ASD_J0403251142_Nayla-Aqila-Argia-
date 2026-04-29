# Implementasi DFS
# Nama: Nayla Aqila Argia
# NIM: J0403251142

# Representasi graph dalam bentuk adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph menggunakan DFS (Depth First Search)

    visited.add(node)          # tandai node sudah dikunjungi
    print(node, end=' ')       # tampilkan node

    # telusuri semua tetangga dari node
    for neighbor in graph[node]:
        if neighbor not in visited:   # jika belum dikunjungi
            dfs(graph, neighbor, visited)  # rekursif ke tetangga tersebut

# set untuk menyimpan node yang sudah dikunjungi
visited = set()

# Menjalankan DFS dari node A
dfs(graph, 'A', visited)