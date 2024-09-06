class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[0] * num_nodes for _ in range(num_nodes)]

    def print_graph(self):
        for row in self.graph:
            print(row)

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def bfs(self, start_node, visited):
        queue = [start_node]
        visited[start_node] = True

        while queue:
            node = queue.pop(0)
            print(node, end=' ')

            for i in range(self.num_nodes):
                if self.graph[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    print("hello")
                    visited[i] = True

    def bfs_disconnected(self):
        visited = [False] * self.num_nodes

        for node in range(self.num_nodes):
            if not visited[node]:
                self.bfs(node, visited)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=' ')

        for i in range(self.num_nodes):
            if self.graph[node][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    def dfs_disconnected(self):
        visited = [False] * self.num_nodes

        for node in range(self.num_nodes):
            if not visited[node]:
                self.dfs(node, visited)


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
    g.bfs_disconnected()
    print("\nDFS is: ")
    g.dfs_disconnected()

