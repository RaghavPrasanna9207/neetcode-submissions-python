# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0 #preidx tells what to create, inidx used as limit
        #preorder follows root left right, which is the order of creation
        #inorder follows left root right, so when root reached in inorder,
        #we know the left part is done, and move to the right part

        def dfs(limit):
            nonlocal preIdx, inIdx #pointers wont be reset
            if preIdx >= len(preorder):
                return None #tree done
            if inorder[inIdx] == limit: #boundary is hit
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val) #build left subtree until this root reached in inorder
            root.right = dfs(limit)
            return root
        return dfs(float("inf"))