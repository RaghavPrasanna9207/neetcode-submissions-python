class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Four conditions: middle element part of left target part of right, me left target left, me right target left, me right target right. Use binary search and do it accordingly.
        # Complexities: O(log n), O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                # 5 6 7 1 2 3 4
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1