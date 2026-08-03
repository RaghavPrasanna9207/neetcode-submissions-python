class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's algorithm is used here. But to handle negative numbers, keep track of the smallest number, as that might become the maximum product if multiplied with another negative number.
        # Complexities: O(n), O(1)
        maxProd, minProd = 1, 1
        res = nums[0]

        for num in nums:
            temp = num * maxProd
            maxProd = max(num, num * maxProd, num * minProd)
            minProd = min(num, temp, num * minProd)
            res = max(res, maxProd)
        return res