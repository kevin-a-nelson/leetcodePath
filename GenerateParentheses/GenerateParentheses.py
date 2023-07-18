
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

        # Why n*2? -> if n = 3, there will be n*2=6 total parentesis in a valid combination. Ex. ((())), ()()()
        # Why n-1? -> The first parent "(" is already added in DP. So if n = 3, we only need to add 5 more parentesis. Ex. ( -> ()()(), ( -> ((()))
        parenthesesToAdd = n * 2 - 1

        for i in range(parenthesesToAdd):
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
