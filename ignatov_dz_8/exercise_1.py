"""1319. Number of Operations to Make Network Connected"""


class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1

        data = list(range(n))

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            data[data[x]] = data[y]

        for edge_1, edge_2 in connections:
            parent_of_u, parent_of_v = find(edge_1), find(edge_2)
            if parent_of_u != parent_of_v:
                union(edge_1, edge_2)

        number_of_components = len(set(find(u) for u in range(n)))
        return number_of_components - 1
