class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # First check for words where the first word is a part of the second word(cat, catch). Have a condition to return nothing for them if present. Make an adjacency graph after that, and then run dfs. Make sure to detect cycles, as they make the language invalid. Mark the visited set true and false, use backtracking. Since this is post order dfs, reverse before returning.
        # Complexities: O(N + V + E), O(V + E)
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ''

        res.reverse()
        return ''.join(res)