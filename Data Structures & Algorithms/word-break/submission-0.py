class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means whether s[i:] can be segmented or not. We go backwards, as we can decide the current one if we know the answer for future positions. Go for a reverse for loop, another one to check each word, check if the length is valid, if the string exists, update dp.
        # Complexities: O(n * m * t), O(n), where n is the lenght, m is the number of words, and t is the max length of a word.
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]