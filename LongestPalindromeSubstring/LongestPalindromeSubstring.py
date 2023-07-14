

# loop through palindrome
# keep track of current palindrome
# return longest palindrome

class Solution(object):

    def isPalindrome(self, str):

        for i in range(len(str) // 2):
            if str[i] != str[len(str) - i - 1]:
                return False

        return True

    def longestPalindrome(self, s):

        if self.isPalindrome(s):
            return s

        longestPalindrome = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):

                if not self.isPalindrome(s[i:j]):
                    continue

                if len(s[i:j]) <= len(longestPalindrome):
                    continue

                longestPalindrome = s[i:j]

        return longestPalindrome


answer = Solution().longestPalindrome("abb")

print(answer)

