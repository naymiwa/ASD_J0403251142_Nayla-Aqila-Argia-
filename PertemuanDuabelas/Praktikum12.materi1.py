# ===============================================
# Materi 1: Algoritma Dijkstra
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Kelas: B2
# ===============================================

import heapq

# Graph berbobot
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Inisialisasi jarak awal semua node = tak hingga
    distances = {node: float('inf') for node in graph}

    # Node awal = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')
print(hasil)