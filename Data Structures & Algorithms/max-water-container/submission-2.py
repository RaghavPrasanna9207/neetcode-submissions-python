class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Complexities: O(n), O(1)      
        # In order to maximise the area, we need 2 containers with a high value. Take two pointers, and move the shorter one inward to calculate the new area and update that.
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res