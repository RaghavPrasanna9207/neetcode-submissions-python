class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # We first build a trie from all the words. Have two sets, one is the visit set, one is the result set. We then start dfs - mark each cell visited, move the trie pointer ahead and add the current character to the word so far. If the word is true, add it to the result set. Then backtrack, remove the cell from the visit set. Run dfs for every cell.
        # Complexities: O(m∗n∗4∗3 ^ t−1 + s), O(s) where m, n are number of rows, columns, t is max length and s is the sum of lengths of all words.
        root = TrieNode()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        visit, result = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            dfs(r - 1, c, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')

        return list(result)