
def bfs_with_list(graph, start):
    print("BFS using list:")
    visited = set()
    queue = [start]  

    while queue:
        current = queue.pop(0)  
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
           
            queue.extend(neighbor for neighbor in graph[current] if neighbor not in visited)
    print("\n")

from collections import deque

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.neighbors = []  

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __hash__(self): 
        return hash(self.name)

    def __eq__(self, other): 
        return self.name == other.name

def bfs_with_deque(start_node):
    print("BFS using deque:")
    visited = set()
    queue = deque([start_node])  

    while queue:
        current_node = queue.popleft()  
        if current_node not in visited:
            print(current_node.name, end=' ')
            visited.add(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    print("\n")

graph = {
    'Start': ['Node1', 'Node2'],
    'Node1': ['Node3', 'Node4'],
    'Node2': ['Node5'],
    'Node3': [],
    'Node4': ['Node5'],
    'Node5': []
}

start = GraphNode('Start')
node1 = GraphNode('Node1')
node2 = GraphNode('Node2')
node3 = GraphNode('Node3')
node4 = GraphNode('Node4')
node5 = GraphNode('Node5')

start.add_neighbor(node1)
start.add_neighbor(node2)
node1.add_neighbor(node3)
node1.add_neighbor(node4)
node2.add_neighbor(node5)
bfs_with_list(graph, 'Start')  
bfs_with_deque(start)         
