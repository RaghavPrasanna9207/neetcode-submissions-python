class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm - if the running sum becomes negative, reset it
        curSum = 0
        maxSub = nums[0]

        for i in nums:
            # append each number
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub
        