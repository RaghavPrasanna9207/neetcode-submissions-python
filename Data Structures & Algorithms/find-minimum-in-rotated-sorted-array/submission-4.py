class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Complexities: O(log n), O(1)
        # Use binary search. Check the difference between l and m. If l is lesser than m, then l to m is sorted and the minimum number is after m. if not, the minimum number is between l and m.
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res