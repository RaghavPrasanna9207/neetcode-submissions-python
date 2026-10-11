class Solution:
    def isHappy(self, n: int) -> bool:
        # Use two pointers to detect a cycle. If they meet at 1, there is no cycle, if not, there is one.
        # Complexities: O(n log n), O(n)
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)

        return True if fast == 1 else False
    
    def sumOfSquares(self, n: int) -> int:
        res = 0

        while n:
            dig = n % 10
            dig = dig ** 2
            res += dig
            n = n // 10

        return res