class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # For storing indices, a hashmap can be used.
        # Complexities: Since a hashmap is used, O(n), O(n) are the time complexities.
        # Approach: Instead of iterating fully, use the target to get the second element.
        # Store elements and indices in the hashmap for quick retrieval.
        indexMap = {}

        for i in range(len(nums)):
            if target - nums[i] in indexMap:
                print(indexMap)
                return [indexMap[target - nums[i]], i]
            indexMap[nums[i]] = i