class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm - if the running sum becomes negative, reset it
        # Complexities: O(n), O(1)
        curSum = 0
        maxSum = nums[0]

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(maxSum, curSum)
        return maxSum