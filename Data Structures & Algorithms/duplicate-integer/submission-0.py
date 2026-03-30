class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeSet = set()

        for i in nums:
            if i in dupeSet:
                return True
            dupeSet.add(i)
        return False