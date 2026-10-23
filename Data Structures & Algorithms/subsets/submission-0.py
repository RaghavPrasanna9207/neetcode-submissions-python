class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Have a recursive function, add the latest element, run recursively, backtrack and run recursively again.
        # Complexities: O(n 2^n), O(n) extra space, O(2^n) output list.
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res