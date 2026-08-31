class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Any number XOR'd with itself gives 0. 1^1 = 0. But 0 ^ x = x. So whatever the number is, which is not in the list, will be the answer. Return the XOR variable. We take it to be n as we do not check that in the loop.
        # Complexities: O(n), O(1)
        
        n = len(nums)
        xor = n

        for i in range(n):
            xor ^= i ^ nums[i]
        return xor