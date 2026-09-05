class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Every number is repeated twice except one. a ^ a = 0. a ^ 0 = a. So XORing everything will give us the answer.
        # Complexities: O(n), O(1)
        res = 0
        for i in nums:
            res = i ^ res
        return res