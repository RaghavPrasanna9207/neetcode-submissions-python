class Solution:
    def numDecodings(self, s: str) -> int:
        # Use the cache to store number of ways to decode the string starting from that particular position(dp[i] -> s[i:]). Take the first digit and add it to the result, if the second digit is valid, take that too and add it to the result. Update the cache and recursively fill all values. Take 1 digit while checking, if the next two digits are in the 10-26 range, take the second digit as well.
        # Complexities: O(n), O(n)
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)