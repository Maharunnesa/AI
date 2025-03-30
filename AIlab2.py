from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_limit(self, node, limit, visited):
        if visited[node]:
            return False
        visited[node] = True

        if limit == 0:
            return True

        for neighbor in self.graph[node]:
            if self.dfs_limit(neighbor, limit - 1, visited):
                return True

        visited[node] = False
        return False

    def topological_sort_IDDFS(self):
        max_depth = len(self.graph)  # Maximum depth for IDDFS
        for depth in range(max_depth):
            visited = {node: False for node in self.graph}
            stack = []
            for node in self.graph:
                if self.dfs_limit(node, depth, visited):
                    stack.append(node)
            if stack:
                return stack[::-1]
        return []

if __name__ == "_main_":
    g = Graph()

    graph_matrix = [
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0],
    ]

    # Convert the matrix to an adjacency list and add edges to the graph
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[0])):
            if graph_matrix[i][j] == 1:
                g.add_edge(i, j)

    # Using IDDFS
    top_order = g.topological_sort_IDDFS()

    print("Topological Order:", top_order)