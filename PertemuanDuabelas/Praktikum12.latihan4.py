# ===============================================
# Nama  : Nayla Aqila Argia
# NIM   : J0403251142
# Kelas : B2
# Praktikum 12 - Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# ===============================================

import heapq

graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
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

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi paling dekat = Kantin (2 menit)
# 2. Waktu ke Aula = 7 menit
# 3. Tidak selalu, karena jalur lebih panjang bisa punya total bobot lebih kecil
# 4. Karena semua bobot positif, jadi Dijkstra cocok digunakan