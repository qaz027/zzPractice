'''
You are provided with a string of alphanumeric characters in which each number, regardless of the number of digits, is always followed by at least one alphabetic character before the next number appears. 
The task requires you to return a transformed version of the string wherein the first alphabetic character following each number is moved to a new position within the string and characters in between are removed.

Specifically, for each number in the original string, identify the next letter that follows it, and then reposition that character to directly precede the number. 
All spaces and punctuation marks between the number and the letter are removed.

The length of the string s ranges from 3 to 106106 (inclusive), and the string contains at least one number. The numbers in the string are all integers and are non-negative.

Here is an example for better understanding:

Given the string:

"I have 2 apples and 5! oranges and 3 grapefruits."

The function should return:

"I have a2pples and o5ranges and g3rapefruits."

In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding the 5 is placed before the 5, and the 'g' subsequent to the 3 is repositioned to precede the 3. 
Punctuation marks and spaces in between are removed.

Please note that the operation should maintain the sequential order of the numbers and the rest of the text. 
Considering this, the task is not solely about dividing a string into substrings but also about modifying them. This will test your expertise in Python string operations and type conversions.
'''

def transform_string(s: str) -> str:
    result = []
    words = s.split()
    digit = ''

    #print(words)

    for word in words:
        if digit:
            result.append(word[0]+digit + word[1:])
            digit = ''  # Reset digit after using it
        else:
            for char in word:
                if char.isdigit():
                    digit += char
            if not digit:
                result.append(word)
            
        # elif word.isdigit():
        #     # If the word is a number, hold it and embed number into the 2nd character of the next word
        #     digit = word
        # else:
        #     print(f"{word} is neither digit or alpha")# If the word is neither a digit nor an alpha, just append it
        #     result.append(word)    

    return " ".join(result)

test_string = "I have 2 apples and 5! oranges and 3 grapefruits."

print(transform_string(test_string))  # Expected output: "I have a2pples and o5ranges and g3rapefruits."

####
# Ignore the following code snippet, it is not part of the solution.
# This is a comment to explain the code snippet below.
# The following code is an incorrect attempt to solve the problem.
# CodeSignal initially told me above code was incorrect but it is actually correct.

'''Nice try! Your approach splits the string by spaces, but the problem says numbers and letters can be separated by spaces or punctuation, and numbers can be anywhere—not just at word boundaries.

    What happens if the number and its following letter are in different "words" after splitting?
    How could you process the string character by character to catch numbers and their following letters, even if there are spaces or punctuation in between?

Try thinking about how you’d track when you’re inside a number, and how to find the first letter after it, no matter what’s in between!
'''

def solution(input_string):
    result = []
    words = input_string.split()
    digit = ''
    cur_word = ''

    for word in words:
        for char in word:
            if digit and char.isalpha():
                result.append(word[0]+digit + word[1:])
                digit = ''  # Reset digit after using it
                cur_word = ''
                
            elif char.isdigit():
                    digit += char
            else:
                cur_word += char
            result.append(cur_word)
            cur_word = ''  # Reset current word after processing

        #if not digit:
            #result.append(word)
        #digit = ''

    return " ".join(result)

#print(solution(test_string))  # Expected output: "I have a2pples and o5ranges and g3rapefruits."