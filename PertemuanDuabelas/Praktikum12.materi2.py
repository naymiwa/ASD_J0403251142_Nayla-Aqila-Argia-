# ===============================================
# Materi 2: Algoritma Bellman-Ford
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Kelas: B2
# ===============================================

# Graph berbobot (bisa negatif)
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    # Inisialisasi jarak
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')
print(hasil)