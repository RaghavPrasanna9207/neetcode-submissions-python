class Solution:
    # Complexities - O(n), O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        # A set can be used for O(1) lookups.
        # It's easier to go backwards instead of forwards while searching for sequence starts.
        # For example, if there's 2, but no 1, then it is the start of a sequence.

        numSet = set(nums)
        lcs = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                lcs = max(length, lcs)
        return lcs