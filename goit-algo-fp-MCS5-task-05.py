import uuid
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


class Node:
    def __init__(self, key, color="blue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def depth_first_traversal(root):
    if root is None:
        return []

    visited = []
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()
        visited.append((node, depth))

        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

    return visited

def breadth_first_traversal(root):
    if root is None:
        return []

    visited = []
    queue = Queue()
    queue.put((root, 0))

    while not queue.empty():
        node, depth = queue.get()
        visited.append((node, depth))

        if node.left:
            queue.put((node.left, depth + 1))
        if node.right:
            queue.put((node.right, depth + 1))

    return visited

def visualize_traversal(traversal):
    num_nodes = len(traversal)
    colors = ['#%02x%02x%02x' % (0, int(255 * (i / num_nodes)), 255) for i in range(num_nodes)] 
    for i, (node, _) in enumerate(traversal):
        node.color = colors[i]

    draw_tree(traversal[0][0])

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)


print("Обхід глибини:")
depth_first = depth_first_traversal(root)
for node, _ in depth_first:
    print(node.val, end=" -> ")
visualize_traversal(depth_first)

print("\nОбхід ширини:")
breadth_first = breadth_first_traversal(root)
for node, _ in breadth_first:
    print(node.val, end=" -> ")
visualize_traversal(breadth_first)
