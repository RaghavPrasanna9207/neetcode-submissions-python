class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Instead of reaching the last item from the first, reach the first item from the last. Keep moving the goal backwards until the first item becomes the goal.
        # Complexities: O(n), O(1)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0