class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A graph is a valid tree if it's fully connected and has no cycles. We will have an adjacency list here, to track all connected nodes. The DFS will go through each node, returns false if it finds a visited ndoe, checks if all nodes are visited, and if so, returns True. It also has to make sure the previous node is not confused as an adjacent node.
        # Complexities: O(V + E), O(V + E)
        if not n:
            return True

        adj = { i: [] for i in range(n)}

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)