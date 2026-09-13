class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Have an adjacency list, go through each node use dfs to visit every connected node. Increment the count for each seperate cycle.
        # Complexities: O(V + E), O(V + E)
        adj = {i: [] for i in range(n)}
        visitSet = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            for j in adj[node]:
                if j not in visitSet:
                    visitSet.add(j)
                    dfs(j)

        count = 0
        for node in range(n):
            if node not in visitSet:
                visitSet.add(node)
                dfs(node)
                count += 1
        return count