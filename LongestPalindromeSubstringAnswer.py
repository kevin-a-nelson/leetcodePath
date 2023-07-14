
def longest_palindrome(input):
    inputLen = len(input)
    # Create a boolean table to store palindrome information
    table = [[False] * inputLen for _ in range(inputLen)]
    
    # All substrings of length 1 are palindromes
    max_length = 1
    start = 0
    for i in range(inputLen):
        table[i][i] = True
    
    # Check for substrings of length 2
    for i in range(inputLen - 1):
        if input[i] == input[i + 1]:
            table[i][i + 1] = True
            max_length = 2
            start = i
    
    # Check for substrings of length 3 or more
    for subStrLen in range(3, inputLen + 1):
        for i in range(inputLen - subStrLen + 1):
            j = i + subStrLen - 1
            print(i,j)
            if input[i] == input[j] and table[i + 1][j - 1]:
                table[i][j] = True
                if subStrLen > max_length:
                    max_length = subStrLen
                    start = i
    
    # Return the longest palindromic substring
    return input[start:start + max_length]

answer = longest_palindrome("abba")

print(answer)