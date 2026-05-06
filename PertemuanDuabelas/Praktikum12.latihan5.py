# ===============================================
# Nama  : Nayla Aqila Argia
# NIM   : J0403251142
# Kelas : B2
# Praktikum 12 - Latihan 5: Studi Kasus Shortest Path
# ===============================================

import heapq

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
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

hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal = Bogor
# 2. Jarak paling kecil = Depok (2)
# 3. Jarak paling besar = Bandung (8)
# 4. Dijkstra bekerja dengan memilih node dengan jarak terkecil dulu, lalu update jarak ke node lain sampai semua node dapat jarak minimum