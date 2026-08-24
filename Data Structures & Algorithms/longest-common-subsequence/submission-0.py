class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Have a graph, whenever letters match, increase count, otherwise take the higher value from either top or left. If both characters match, the value of the cell is 1 + value of top left diagonal cell.
        # Complexities: O(n * m), O(n * m)
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[len(text1)][len(text2)]