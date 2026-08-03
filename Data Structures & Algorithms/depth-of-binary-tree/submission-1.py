# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Check the current node. If not, return 0. Check the children recursively, adding a 1. This will give the length.
        # Complexities: O(n), O(h)
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))