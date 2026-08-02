class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using a sliding window here. Use a for loop to traverse the string with the r pointer, while adding elements to a hashmap. If there are duplicates, move the l pointer till there are none. Remove and add from the set as necessary. Calculate the result by comparing the maximum value with r - l + 1 at each point.
        # Complexities: O(n), O(m) where n is the length of the string and m is the number of unique characters in the string.
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res