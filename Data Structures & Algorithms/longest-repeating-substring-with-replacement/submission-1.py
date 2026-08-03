class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Firstly, only a number is needed, no need to change the string. We can work under assumption here. For the window, take the count of the most frequent character. That added to k is the maximum window size. Size - count cannot be more than k. We basically log the frequency, go through every window and check for the maximum
        # Complexities: O(n), O(m), where n is the length and m is the total number of unique characters.

        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res