''' 
Processing Words in Sentences with Nested Loops
Introduction

Hello and welcome to today's Python lesson! We are going to dive into a delightful challenge that will test our abilities in string manipulation, more specifically in a 
concept known as nested loops. Prepare yourself for an interesting journey as we explore how to extract odd-indexed characters from each word in a sentence, but only if 
the word has an even number of characters. Doesn't it sound exciting? Let's get started!

Task Statement

Here is a detailed look at our task: We will work with a string that represents a sentence in which words are separated by spaces. Your task is to create a Python function 
that identifies the odd-indexed characters of words that have an even number of characters. Then, combine these characters into a single string, maintaining the order in 
which they appear in the sentence.

Let's consider an example to foster a deep understanding: "Python is a high-level programming language." Here, the word 'Python' has 6 characters (an even number), 
and we will select the odd-indexed characters from this word, specifically, 'y', 'h', and 'n'. Similarly, we select 's' from 'is', and 'i', 'h', 'l', 'v', 'l' from 'high-level'. 
The words 'a', 'programming', and 'language.' have odd lengths, so they are skipped.

So, if our function is working correctly, it should return "yhnsihlvl". This task highlights the versatility of loops and conditionals in solving all kinds of string challenges!

Let's get started!
Solution Building: Step 1

We initiate our solution-building process by splitting the sentence into words. Python provides us with a built-in split() function that makes this task easy. 
The function separates the sentence into words at each space, providing us with a list containing all the words in the sentence.


Python

def solution(sentence):
    words = sentence.split(' ')
    # we will proceed progressively

Solution Building: Step 2

Now we delve into nested loops: an outer loop that iterates over every single word, and an inner loop that checks every character within each word. 
Firstly, we'll use an if condition that verifies whether a word has an even length. How do we do this, you ask? By finding the modulus of the length of the word with 2. 
If this modulus is zero, our word has an even length!

Python

def solution(sentence):
    words = sentence.split(' ')
    for word in words:
        if len(word) % 2 == 0:  # confirms whether the length of the word is even
            # we are building up our solution progressively

Solution Building: Step 3

With our outer loop set, it's time to complete our inner loop. We intend to iterate over only the odd-indexed characters in each word of even length. 
To accomplish this, we start from an index of 1 and increment by 2 each time. This strategy ensures our loop only selects the characters at odd indexes.

We then append these characters to our result string, which will be returned as our final output.

Python

def solution(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 0:  # check if the length of word is even
            for i in range(1, len(word), 2):  # loop over odd characters
                result += word[i]

    return result

Lesson Summary

Bravo! You've just successfully navigated through the maze of nested loops to extract specific information from words within a sentence. 
You've learned how to analyze a sentence by breaking it down into its constituent words and then studying each word at an even deeper level.

Now, use this knowledge as a foundation in your exploration of nested loops. Practicing more is key, as the more you apply what you've learned, 
the more you will reinforce this knowledge. Are you ready to dive deeper into the world of nested loops and string manipulations? Let's dive right in!
'''

'''Exercise 1

In this task, we are manipulating sentences and strings using nested loops. You will be given a string representing a sentence where words are separated by spaces. 
Your objective is to write a Python function that selects the even-indexed characters of words containing an odd number of characters.

This sentence string will have a maximum length of 500 characters, including spaces.

Subsequently, these characters must be combined into a single string in the order they appear in the sentence, 
but the final output string will be reversed end-to-end.

For instance, if the input sentence is "Coding tasks are fun and required", the output string should be "tssaefnad", 
which, when reversed, becomes "danfeasst". The words "tasks", "are", "fun", and "and" are selected since they have an odd number of characters, 
and the characters 't', 's', 's', 'a', 'e', 'f', 'n', 'a', 'd' at even indexes are chosen and then reversed in the final string. 
Do not forget that Python indexing begins at 0, so 't' in "tasks" is considered to be at an even index. 
Single-character words must also be taken into consideration for this task.

Are you ready to accept the challenge and create a solution that efficiently accomplishes this task step by step?'''

def reversed_characters_return(sentence):
    words = sentence.split(' ')
    result = ''

    for word in words:
        if len(word) % 2 == 1: # only consider odd-length words
            for i in range(0, len(word), 2):  # loop over even
                result += word[i]  # append even-indexed characters

    return result[::-1]  # Return the result string reversed

''' Example 2

You are given a string of n words, with n ranging from 1 to 100, inclusive. The words are separated by a single space in the string. 
Your task is to return the most frequently occurring character in each word that has an odd number of characters. 
The resulting characters should be concatenated into a string with their occurrences in the sentence.

Please note:

    Each word's character count ranges from 1 to 500, inclusive. The string contains lowercase and uppercase alphanumeric characters, spaces, and punctuation.
    For instance, if the input string is "Hello world this is a demo string", your function should return "lwa". 
    In this string, 'Hello', 'world', and 'a' have an odd number of characters. The most frequently occurring character in these words are 'l', 'w', and 'a' respectively. 
    When concatenated, they form "lwa".

    In case of a tie in character frequency, return the character that appears first in the word. In the example above, we took 'w' from the word 'world'.
    The function should be case insensitive. The lowercase and uppercase characters should be counted as the same character. The output should only contain lowercase characters. 
    For example: "Hhi" should return "h" because "h" appears twice in the string even though one is uppercase and one is lowercase.
    
    If there are no words with an odd number of characters in the input string, your function should return an empty string.
    The input string will always be at least one character long, and it cannot be just a single whitespace.

Having a good understanding of string operations and the use of nested loops is very useful in solving this task.'''

# def most_frequent_char(sentence):         # this doesn't work as expected
#     words = sentence.split(' ')
#     result = ''
#     print(f"Words from sentence: {words}")

#     for word in words:
#         print(f"Processing word: {word}")
#         if len(word) % 2 == 1: # only consider odd-length words
#             char_count = {}
#             for char in word.lower():
#                 print(f"Counting character: {char}")
#                 if char.isalnum():
#                     char_count[char] = char_count.get(char, 0) + 1
#             if char_count:  # if there are characters to consider
#                 print(f"Character counts: {char_count}")
#                 print(f"going to find the most frequent character in: {word}")
#                 print(f"Max of character count: {max(char_count)}")
#                 most_frequent = max(char_count, key=lambda k: (char_count[k], -word.index(k)))
#                 print(f"Most frequent character in '{word}': {most_frequent}")
#                 result += most_frequent

#     return result.lower()  # Return the result string in lowercase

# sample = "Hello world this is a demo string"

# print(most_frequent_char(sample))  # Output: "lwa"

def most_frequent_char2(sentence):
    words = sentence.split(' ')
    result = ''
    most_freq = ''
    print(f"Words from sentence: {words}")

    for word in words:
        print(f"Processing word: {word}")
        if len(word) % 2 == 1: # only consider odd-length words
            char_count = {}
            for char in word.lower():
                print(f"Counting character: {char}")
                if char.isalnum():
                    char_count[char] = char_count.get(char, 0) + 1
            if char_count:  # if there are characters to consider
                most_freq = list(char_count.keys())[0]
                most_freq_count = list(char_count.values())[0]
                for key, value in char_count.items():
                    print(f"Character: {key}, Count: {value}")
                    if value > most_freq_count:
                        most_freq = key
                        most_freq_count = value
                    print(f"Updated most frequent character: {most_freq} with count: {most_freq_count}") 

                print(f"Most frequent character in '{word}': {most_freq} with a count of {most_freq_count}")
                result += most_freq

    return result.lower()  # Return the result string in lowercase

sample = "Hello world this is a demo string"

print(most_frequent_char2(sample))  # Output: "lwa"


''' Exercise 3

You are given a string that represents a sentence in which words are separated by spaces. Your task is to create a Python function that identifies and concatenates the second half 
of each word with an even number of characters, ensuring the characters of this second half go before the character c in the ASCII table. 
Then, combine these characters into a single string, maintaining the order in which they appear in the sentence.

The input sentence consists of ASCII characters from the space character (' ') up to the tilde character ('~'), with its length ranging between 1 and 500, inclusive. 
These characters form words separated by spaces, without any consecutive space characters.

For example, consider the sentence: "Python is a high-level programming language." and the character "n". The word 'Python' consists of 6 characters (an even number), 
and the second half of this word is 'hon'. In this second half, only 'h' is less than 'n'.

The output of your function, in this case, should be: "h", as it's the only character that meets the conditions.

For the character comparison ('<' character), use the ASCII values since all characters in the sentence are ASCII. 
ASCII codes for characters can be found by using Python's built-in function ord().'''

def weird_fucking_problem(sentence, c):
    words = sentence.split(' ')
    result = ''
    c_ord = ord(c)  # Get the ASCII value of character c

    for word in words:
        if len(word) % 2 == 0:
            second_half = word[len(word)//2:]
            for char in second_half:
                if ord(char) < c_ord:
                    result += char
    
    return result