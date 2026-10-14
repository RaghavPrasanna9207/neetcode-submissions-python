# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Use dfs and return a list, with the first element being the balanced boolean, and the second being the height. Calculate left and right heights in the dfs function, and the balanced variable is calculated by checking the height difference, and if any of the children return false.
        # Complexities: O(n), O(h)
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]