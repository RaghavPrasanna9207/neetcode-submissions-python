class Solution:

    # Complexities - O(n), O(n)
    # Approach - Adding to sets and retrieving data from them are O(n) operations. 
    # Additionally, they do not have duplicates.
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeSet = set()

        for i in nums:
            if i in dupeSet:
                return True
            dupeSet.add(i)
        return False