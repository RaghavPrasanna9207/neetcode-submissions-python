class Solution:
    def countSubstrings(self, s: str) -> int:
        # Use two pointers, start at the centre and go left and right. Check for odd and even palindrome. Increment the count.
        # Complexities: O(n^2), O(1)
        count = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count