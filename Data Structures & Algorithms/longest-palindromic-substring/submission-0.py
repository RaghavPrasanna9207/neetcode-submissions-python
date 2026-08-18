class Solution:

    # Use two pointers. Start from each character, go right and left and check. Update the index and length each iteration. Check for odd and even palindromes.
    # Complexity: O(n^2), O(1) extra space, O(n) for output string.
    def longestPalindrome(self, s: str) -> str:
        resIndex = 0
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIndex = l
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIndex = l
                l -= 1
                r += 1
        return s[resIndex: resIndex + resLen]