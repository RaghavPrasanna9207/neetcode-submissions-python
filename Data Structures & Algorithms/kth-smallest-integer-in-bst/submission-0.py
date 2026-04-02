# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack: #neither should be empty
            while cur:
                stack.append(cur)
                cur = cur.left #keep going left and add elements till there is no more left element

            cur = stack.pop() #if nothing, pop it. this is the first element
            #order of popping = k order
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right #go to right subtree