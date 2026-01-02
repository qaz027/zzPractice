'''
Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). 
Each word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from 1 to 26. 
Your task is to parse this string and swap the type of each word: convert numbers into their corresponding English alphabet letters, and letters into their numerical equivalents. 
This means '1' should convert to 'a', and 'a' should convert to '1'.

You need to return a new string with the converted words, rejoined with hyphens.

Ensure you maintain the original order of the words from the input string in your output string.

The input string's length should range from 1 to 1000 for this exercise. The string will never be empty, always containing at least one valid lowercase letter or numerical word.

Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their corresponding letters from 'a' to 'z', and vice versa.

Example

For the input string "1-a-3-c-5", the output should be "a-1-c-3-e".'''

def swap_words(input_string):
    words = input_string.split('-')
    result = []

    for word in words:
        if word.isdigit():  # Check if the word is a number
            num = int(word)
            if 1 <= num <= 26:  # Convert number to letter
                result.append(chr(num + 96))  # 'a' is chr(97), so we add 96
            else:
                result.append(word)  # If out of range, keep as is
        elif word.isalpha() and len(word) == 1:  # Check if the word is a single letter
            result.append(str(ord(word) - 96))  # Convert letter to number
        else:
            result.append(word)  # Keep other words unchanged

    return '-'.join(result)  # Join the transformed words with hyphens

def solution(s):
    word_num = s.split('-')
    result = []
    
    for digit in word_num:
        if digit.isdigit():
            num = int(digit)
            # convert number to corresponding letter (1-26) -> (a-z)
            result.append(chr(num+96))
            
        if digit.isalpha():
            result.append(str(ord(digit)-96))
            
    return '-'.join(result)