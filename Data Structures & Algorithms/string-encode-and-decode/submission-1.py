class Solution:
    # Complexities: O(m), O(m + n), where m is sum of lengths, n is number of strings.
    # For encoding, let the string be length + delimiter + string for all. This will make it easy to seperate the string and the length and easy to track as well.
    # For decoding, traverse till the delimiter to get the length, use the length to get the string. Repeat by updating the two pointers i and j.
    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res