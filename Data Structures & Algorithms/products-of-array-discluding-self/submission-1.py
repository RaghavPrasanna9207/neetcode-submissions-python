class Solution:
    # Complexities: O(n), O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Each element is the product of all elements before, and all elements after.
        # We can have two arrays for this, one for the prefixes and one for the suffixes.

        n = len(nums)
        prefixes = [0] * n
        suffixes = [0] * n

        prefixes[0] = suffixes[n - 1] = 1

        for i in range(1, n):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]

        result = [0] * n

        for i in range(n):
            result[i] = prefixes[i] * suffixes[i]
        return result