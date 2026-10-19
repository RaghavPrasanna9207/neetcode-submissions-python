class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Use binary exponentiation - repeated squaring. If the number is odd, multiply the result by x one more time.
        # Complexities: O(log n), O(1)
        if x == 0:
            return 0

        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power:
            if power & 1:
                res *= x
            x *= x
            power >>= 1

        return res if n >= 0 else 1/res