class WordDictionary:
    # For the search, use a DFS. There are two ways. One: If it is a '.', then use dfs and check for each following letter. If not, check in the usual way we do for a trie.
    # Complexities: O(n), O(t + n), where n is the length of the string and t is the total number of trie nodes.
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False