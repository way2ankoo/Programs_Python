class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    def add_edge(self, u, v):
        # check if u exists
        if u not in self.graph:
            self.graph[u] = []

        # add u -> v
        self.graph[u].append(v)

        # If undirected graph
        if v not in self.graph:
            self.graph[v] = []

        self.graph[v].append(u)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
        # print(max(self.graph))

    def bfs_disconnected(self):
        visited = [False] * len(self.graph)

        for node in self.graph:
            if not visited[node]:
                self.bfs(node, visited)

    def bfs(self, start_node, visited):
        queue = [start_node]
        # visited = [False] * len(self.graph)
        visited[start_node] = True

        while queue:
            popped = queue.pop(0)
            print(f"{popped},", end=" ")

            for neighbor in self.graph.get(popped):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs_disconnected(self):
        visited = set()

        for node in self.graph:
            if node not in visited:
                self.dfs_rec(node, visited)

    def dfs(self, start_node):
        visited = set()
        self.dfs_rec(start_node, visited)

    def dfs_rec(self, node, visited):
        visited.add(node)
        print(f"{node},", end=" ")

        for neighbor in self.graph.get(node):
            if neighbor not in visited:
                self.dfs_rec(neighbor, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()
g.bfs(0)
print()
g.dfs(0)
