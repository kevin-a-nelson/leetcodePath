
class Solution:

    def isValidParenthesis(self, parentheses):

        stack = []
        for paren in parentheses:
            if stack == [] and paren == ")":
                return False

            if paren == "(":
                stack.append("(")
            else:
                stack.pop()

        return stack == []

    def generateParentheses(self, n):
        DP = [["("]]

        for i in range(3 * 2 - 1):
            DP.append([])
            for paren in ["(", ")"]:
                for combination in DP[i]:
                    DP[i+1].append(combination + paren)

        validParenthesis = []
        for combination in DP[-1]:
            if not self.isValidParenthesis(combination):
                continue

            validParenthesis.append(combination)

        return validParenthesis


solution = Solution().generateParentheses(3)

print(solution)
