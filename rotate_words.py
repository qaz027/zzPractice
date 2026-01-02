'''
You are given a string of n characters, with n varying from 1 to 1000, inclusive. Your task is to write a Python function that takes this string as input, applies the following operations, and finally returns the resulting string.

    Split the given string into individual words, using a space as the separator.
    Convert each word into a list of its constituent characters, and shift each list once to the right (with the last element moving to the first position).
    After the rotations, reassemble each word from its list of characters.
    Join all the words into a single string, separating adjacent words with a single space.
    Return this final string as the function's output.

The constraints for the problem are as follows:

    The input string will neither start nor end with a space, nor will it have multiple consecutive spaces.
    Each word will contain only alphabets and digits, and its length will range from 1 to 10.
    The words are case-sensitive; for example, 'word' and 'Word' are considered distinct.

Your program should output a single string with the words rotated by their lengths while preserving their original order.

As an illustration, consider the input string "abc 123 def". Applying the stated operations results in the output "cab 312 fde".
'''

def rotate_words(input_string):    # Split the input string into words
    words = input_string.split()
    
    # Rotate each word
    rotated_words = []
    for word in words:
        # Convert the word to a list of characters
        char_list = list(word)
        # Rotate the list to the right by one position
        if len(char_list) > 1:
            char_list.insert(0, char_list.pop())
        # Join the characters back into a word
        rotated_word = ''.join(char_list)
        rotated_words.append(rotated_word)
    
    # Join all rotated words into a single string with spaces
    result_string = ' '.join(rotated_words)
    
    return result_string

def rotate_words2(input_string):
    return ' '.join(''.join([word[-1]] + list(word[:-1])) for word in input_string.split())

# Example usage
print(rotate_words("abc 123 def"))  # Output: "cab 312 fde"
print(rotate_words2("abc 123 def"))  # Output: "cab 312 fde"

