

class Solution(object):

    def longestPalindrome(self, inputStr):

        # make matrix with the number of cols and rows as the length of the string
        inputStrLen = len(inputStr)
        isPalindrome = [[False] * inputStrLen for _ in range(inputStrLen)]

        # make every single character palindrome true in the matrix
        maxPalindromeLen = 1
        maxPalindromeStart = 0
        for i in range(inputStrLen):
            isPalindrome[i][i] = True

        # make every two character palindrome true in the matrix
        for i in range(inputStrLen - 1):
            if inputStr[i] == inputStr[i+1]:
                isPalindrome[i][i+1] = True
                maxPalindromeStart = i
                maxPalindromeLen = 2

        # make every 3 or more character palindrome true in the matrix
        # loop subStrLen from 3 to len of inputStr
        for subStrLen in range(3, inputStrLen + 1):
            for subStrStart in range(inputStrLen - subStrLen + 1):
                subStrEnd = subStrStart + subStrLen - 1

                if inputStr[subStrStart] != inputStr[subStrEnd]:
                    continue

                if not isPalindrome[subStrStart + 1][subStrEnd - 1]:
                    continue

                isPalindrome[subStrStart][subStrEnd] = True

                if maxPalindromeLen > subStrLen:
                    continue

                maxPalindromeStart = subStrStart
                maxPalindromeLen = subStrLen
        
        return inputStr[maxPalindromeStart:maxPalindromeStart + maxPalindromeLen]


