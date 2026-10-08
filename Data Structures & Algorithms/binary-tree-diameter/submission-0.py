# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Calculate left + right at each node using dfs, keep track of the maximum.
        # Complexities: O(n), O(h)
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter