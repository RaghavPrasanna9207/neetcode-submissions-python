class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Have a result, a carry and a mask. In a loop, take each bit and add them, and the carry. Update the carry, and update each bit into the result. At the end, if it's negative, flip it.
        # Complexities: O(1), O(1)
        res = 0
        carry = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            current = aBit ^ bBit ^ carry
            carry = (aBit + bBit + carry) >= 2

            if current:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res