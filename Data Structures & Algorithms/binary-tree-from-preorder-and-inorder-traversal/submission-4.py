# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The preorder list always has the node at the start. So take the node first. After that, the left subtree's node is there at the start. So recursively we can determine the start of each subtree. But to know when it's the left or the right subtree, we need the inorder list. Find the root in the inorder list, go left to get the left subtree's elements. Use a hashmap for the inorder indices, for quick lookup.
        # Complexities: O(n), O(n)

        indices = {val: idx for idx, val in enumerate(inorder)}
        self.preIndex = 0

        def dfs(l, r):
            if l > r:
                return None

            rootValue = preorder[self.preIndex]
            self.preIndex += 1

            root = TreeNode(rootValue)
            mid = indices[rootValue]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)