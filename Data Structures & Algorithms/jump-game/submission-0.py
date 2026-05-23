class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # instead of reaching the last from the first, go reverse
        goal = len(nums) - 1
        # keep moving the goal until it reaches the first. if it cant reach, return false

        for i in range(len(nums) - 2, -1, -1): # start at second last element
            if i + nums[i] >= goal:
                # goal can be reached by i
                goal = i # move back
        return goal == 0