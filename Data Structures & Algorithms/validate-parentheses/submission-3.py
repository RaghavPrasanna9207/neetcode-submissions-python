class Solution:
    # Complexities - Use a stack for O(n), O(n)
    # When an opening bracket is encountered, add it to the stack. Pop it when the corresponding closing bracket is found.
    # Use a dict to track closing brackets. Pop and append as needed.
    def isValid(self, s: str) -> bool:
        parDict = {')':'(', ']':'[', '}':'{'}
        stack = []

        for i in s:
            if i in parDict:
                if stack and stack[-1] == parDict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False