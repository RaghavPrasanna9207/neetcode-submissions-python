class Solution:
    # Complexities: O(n), O(1). Creating any copy of the string would make it O(1), which is to be avoided.
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers. One at the start, one at the end. Skip anything not alnum and take lower while comparing to make sure the cases match. Move the pointers towards each other.
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True