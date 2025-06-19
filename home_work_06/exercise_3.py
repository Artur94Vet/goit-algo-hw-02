# Опис завдання
'''
Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
'''
# Виконання завдання


import networkx as nx
import matplotlib.pyplot as plt
import heapq
import pandas as pd

# --- Побудова графа метро з вагами ---
G = nx.Graph()

# Станції та ваги (час у хвилинах між станціями)
edges_with_weights = [
    ("Академмістечко", "Житомирська", 3),
    ("Житомирська", "Святошин", 2),
    ("Святошин", "Нивки", 3),
    ("Нивки", "Берестейська", 2),
    ("Берестейська", "Шулявська", 2),
    ("Шулявська", "Політехнічний інститут", 3),
    ("Політехнічний інститут", "Вокзальна", 2),
    ("Вокзальна", "Університет", 2),
    ("Університет", "Театральна", 1),
    ("Театральна", "Хрещатик", 2),
    ("Хрещатик", "Арсенальна", 3),
    ("Хрещатик", "Майдан Незалежності", 1),
    ("Театральна", "Золоті ворота", 1)
]

# Додавання ребер з вагами
for u, v, w in edges_with_weights:
    G.add_edge(u, v, weight=w)

# --- Реалізація алгоритму Дейкстри ---
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# --- Обчислення всіх найкоротших шляхів ---
all_shortest_paths = {}
for node in G.nodes:
    all_shortest_paths[node] = dijkstra(G, node)

# --- Вивід у вигляді таблиці ---
df_dijkstra = pd.DataFrame(all_shortest_paths).round(1)
print("=== Найкоротші шляхи між усіма станціями (у хвилинах) ===")
print(df_dijkstra)

# --- Візуалізація графа ---
plt.figure(figsize=(14, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1600, node_color='lightblue', font_size=10, edge_color='gray', width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=9)
plt.title("Київське метро — найкоротші шляхи (алгоритм Дейкстри)", fontsize=14)
plt.show()
