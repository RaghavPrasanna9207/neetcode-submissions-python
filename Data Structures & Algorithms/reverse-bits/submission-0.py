class Solution:
    def reverseBits(self, n: int) -> int:
        # Since it's a 32 bit unsigned integer, we will extract each bit by using (n >> i) & 1 - this right shifts and adds 1, checking if the digit is 1 or 0 - then add that to the result, by left shifting it the correct number of times before adding.
        # Complexities: O(n), O(n)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res