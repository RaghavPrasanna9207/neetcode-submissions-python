class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Pick a number which has not been used, add it to the current permutation, continue building. When a full permutation is reached, add it to the list. After each choice, backtrack.
        # Complexities: O(n! * n), O(n! * n)
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False