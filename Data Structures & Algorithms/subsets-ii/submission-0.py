class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Classic backtracking, but before excluding a number, make sure to skip all duplicates.
        # Complexities: O(n * 2^n), O(n) extra space, O(2^n) for output list.
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res