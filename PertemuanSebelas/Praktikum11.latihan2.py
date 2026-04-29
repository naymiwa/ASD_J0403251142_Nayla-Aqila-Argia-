# Praktikum 11 - Latihan 2 (DFS)
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)

# Jawaban Pertanyaan:
# 1. DFS masuk ke node terdalam dulu karena:
#    menggunakan rekursi (stack)
#    sehingga selalu lanjut ke tetangga sebelum kembali
#
# 2. Jika urutan neighbor diubah:
#    hasil urutan DFS juga berubah
#
# 3. Perbandingan BFS vs DFS:
#    BFS: A B C D E F (melebar)
#    DFS: A B D E C F (menyelam)