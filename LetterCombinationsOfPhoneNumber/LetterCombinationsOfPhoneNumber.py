

class Solution():
    
    def letterCombinations(self, digits):

        if digits == "":
            return []

        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combinations = [[] for _  in range(len(digits) + 1)]

        combinations[0].append('')

        for digitIndex in range(len(digits)):
            for letter in digitsToLetters[digits[digitIndex]]:
                for combination in combinations[digitIndex]:
                    combinations[digitIndex + 1].append(combination + letter)
        
        return combinations[len(digits)]



solution = Solution().letterCombinations("234")

print(solution)

