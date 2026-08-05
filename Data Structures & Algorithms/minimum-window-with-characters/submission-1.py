class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Complexities: O(n + m), O(k) where n and m are the lengths of strings s and t, k is the total number of unique characters.
        # Have two hashmaps to compare the frequencies and perform a sliding window operation. ALso have two variables 'have' and 'need' to track the amount of characters in the map and needed in the map respectively. Finally, have an array and a count variable to track the starting position, the ending position, and the length of the window. Move the right pointer forward, and when the frequencies match, move the left pointer forward, logging all the window values.
        if t == "":
            return ""

        countT = {}
        window = {}

        for i in t:
            countT[i] = countT.get(i, 0) + 1

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""