class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # At any given moment, we have two decisions - add an opening or a closing paranthesis, provided they don't break any rules. Use a recusrive functions with two if conditions - one if an open bracket can be added, and one if a closed one can be added.
        # Complexities: O((4 ^ n)/root(n)), O(n)
        stack = []
        res = []

        def backtrack(openp, closep):
            if openp == closep == n:
                res.append("".join(stack))
                return

            if openp < n:
                stack.append("(")
                backtrack(openp + 1, closep)
                stack.pop()

            if closep < openp:
                stack.append(")")
                backtrack(openp, closep + 1)
                stack.pop()

        backtrack(0, 0)
        return res