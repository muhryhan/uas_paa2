# Muhammad Ryhan
# F5121008
import time
import itertools
import heapq

# Fungsi untuk menampilkan graf
def display_graph(graph):
    for node in graph:
        print(node, "->", graph[node])

# Algoritma TSP (Brute Force)
def tsp(graph):
    nodes = list(graph.keys())
    permutations = list(itertools.permutations(nodes))
    shortest_path = None
    shortest_distance = float('inf')
    start_time = time.time()

    for path in permutations:
        distance = 0
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i+1]
            if next_node in graph[current_node]:
                distance += graph[current_node][next_node]
            else:
                distance = float('inf')
                break
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    end_time = time.time()
    execution_time = end_time - start_time

    print("TSP (Brute Force):")
    print("Waktu komputasi:", execution_time, "detik")
    print("Jalur terpendek:", shortest_path)
    print("Jarak terpendek:", shortest_distance)
    print()

    # Analisis algoritma TSP
    print("Analisis Algoritma TSP (Brute Force):")
    print("Worst case: O(n!)")
    print("Best case: O(n!)")
    print("Average case: O(n!)")
    print()

# Algoritma Dijkstra
def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    heap = [(0, start_node)]
    visited = set()
    shortest_path = {}
    start_time = time.time()

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        visited.add(current_node)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    end_time = time.time()
    execution_time = end_time - start_time

    print("Dijkstra:")
    print("Waktu komputasi:", execution_time, "detik")
    print("Jarak terpendek dari", start_node, "ke setiap node:")
    print(distances)
    print()

    # Analisis algoritma Dijkstra
    print("Analisis Algoritma Dijkstra:")
    print("Worst case: O((V + E) log V), di mana V adalah jumlah simpul dan E adalah jumlah tepi")
    print("Best case: O((V + E) log V)")
    print("Average case: O((V + E) log V)")
    print()

# Graf yang diberikan
graph = {
    'A': {'B': 3, 'C': 5, 'D': 2},
    'B': {'A': 3, 'C': 9, 'D': 4},
    'C': {'A': 5, 'B': 9, 'D': 6},
    'D': {'A': 2, 'B': 4, 'C': 6}
}

print("Graf:")
display_graph(graph)
print()

while True:
    print("Pilihan:")
    print("1. TSP (Brute Force)")
    print("2. Dijkstra")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == "1":
        tsp(graph)
        break
    elif choice == "2":
        start_node = input("Masukkan simpul awal: ")
        if start_node in graph:
            dijkstra(graph, start_node)
            break
        else:
            print("Simpul awal tidak valid. Silakan masukkan simpul yang benar.")
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")