# ===============================================
# Nama  : Nayla Aqila Argia
# NIM   : J0403251142
# Kelas : B2
# Praktikum 12 - Latihan 3: Implementasi Bellman-Ford
# ===============================================

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Bobot langsung A ke B = 5
# 2. Jalur A -> C -> B = 4 + (-2) = 2
# 3. Jalur lewat C lebih kecil
# 4. Karena Bellman-Ford melakukan relaksasi semua edge berulang,
#    jadi tetap bisa menemukan jarak minimum walaupun ada bobot negatif
# 5. Relaksasi = proses update jarak kalau ada jalur yang lebih pendek
# 6. Dijkstra lebih cepat tapi tidak bisa negatif, Bellman-Ford lebih fleksibel tapi lebih lambat