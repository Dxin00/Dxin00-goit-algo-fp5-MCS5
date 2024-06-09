import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        shortest_paths = {node: (float('inf'), None) for node in self.nodes}
        shortest_paths[start] = (0, None)
        priority_queue = [(0, start)]

        while priority_queue:
            current_weight, current_node = heapq.heappop(priority_queue)

            if current_weight > shortest_paths[current_node][0]:
                continue

            if current_node in self.edges:
                for neighbor, weight in self.edges[current_node]:
                    weight += current_weight
                    if weight < shortest_paths[neighbor][0]:
                        shortest_paths[neighbor] = (weight, current_node)
                        heapq.heappush(priority_queue, (weight, neighbor))

        return shortest_paths

    def visualize_shortest_paths(self, start_node):
        shortest_paths = self.dijkstra(start_node)
        
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node)
        for from_node, edges in self.edges.items():
            for to_node, weight in edges:
                G.add_edge(from_node, to_node, weight=weight)

        edge_labels = {}
        paths = {}
        for node, (distance, previous) in shortest_paths.items():
            if previous is not None:
                G.add_edge(previous, node, color='red', weight=distance)
                edge_labels[(previous, node)] = distance
                
                path = []
                current = node
                while current is not None:
                    path.append(current)
                    current = shortest_paths[current][1]
                path.reverse()
                paths[node] = path

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
        edge_weights = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_color='black', font_size=10)
        plt.title("Shortest Paths Visualization")
        plt.show()
        
        print("Побудова шляхів від", start_node)
        min_distance = float('inf')
        min_path = None
        for node, path in paths.items():
            distance = shortest_paths[node][0]
            print("До точки", node, ":", path, "дистанція:", distance,'км')
            if distance < min_distance:
                min_distance = distance
                min_path = path
        print("Найкоротший шлях:", min_path, "дистанція:", min_distance,'км')

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge("A", "B", 6)
graph.add_edge("A", "D", 1)
graph.add_edge("B", "D", 2)
graph.add_edge("B", "E", 2)
graph.add_edge("B", "C", 5)
graph.add_edge("D", "E", 1)
graph.add_edge("E", "C", 5)

start_node = "A"
graph.visualize_shortest_paths(start_node)
