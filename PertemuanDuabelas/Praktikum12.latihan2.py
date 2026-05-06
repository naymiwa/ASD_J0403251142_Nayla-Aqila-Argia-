# ===============================================
# Nama  : Nayla Aqila Argia
# NIM   : J0403251142
# Kelas : B2
# Praktikum 12 - Latihan 2: Implementasi Dijkstra
# ===============================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Jarak A ke B = 4
# 2. Jarak A ke C = 2
# 3. Jarak A ke D = 3
# 4. Karena lewat C lebih kecil (2 + 1 = 3) dibanding lewat B (4 + 5 = 9)
# 5. priority_queue berfungsi untuk mengambil node dengan jarak paling kecil dulu
# 6. Dijkstra tidak cocok untuk bobot negatif karena pakai greedy, jadi bisa salah menentukan jalur