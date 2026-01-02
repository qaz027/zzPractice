''' Lesson: Frequency Calcs and Multi-step processes 

Frequency Calculation and Multi-Step Operations
Introduction

Hello! Are you ready for an exciting voyage into the wonderful realm of strings and data structures? 
Today, we will be assisting Alice, an aspiring cryptographer, with an intriguing string manipulation task. 
She loves playing with strings and has come up with a unique string encoding scheme. I assure you, this will be an enlightening journey that will stretch your programming muscles. 

Let's get started!

Task Statement

Alice has devised a unique way of encoding words. She takes a word and replaces each character with the next character in the alphabetical order. 
In other words, given a string word, for each character, if it's not z, she replaces it with the character that comes next alphabetically. For the character z, she replaces it with a.

Another element of Alice's algorithm involves frequency analysis. After shifting the characters, she counts the frequency of each character in the new string. 
Then, she creates an association of each character with its frequency and ASCII value. Each character maps to a number, 
which is a product of the ASCII value of the character and its frequency. The aim of our task is to construct a list that contains these products, sorted in descending order.

Example

For the input string "banana", the output should be [294, 222, 99].

The string "banana" will be shifted to "cbobob".

Calculating the product of frequency and ASCII value for each character:

    The ASCII value for 'c' is 99, it appears once in the string so its product is 99x1 = 99.
    The ASCII value for 'b' is 98, it appears three times in the string so its product is 98x3 = 294.
    The ASCII value for 'o' is 111, it appears twice in the string so its product is 111x2 = 222.

Collecting these products into a list gives [99, 294, 222]. Sorting this list in descending order results in [294, 222, 99].
Solution Building: Step 1 - Mapping each character to the next alphabetical character

Our first step involves mapping each character of the input string to the next alphabetical character. 
For this, we define the next_string as an empty string, storing the result of the shift operation. We then iterate over each character of the input string. 
If a character is not z, we replace it with the next alphabetical character using the built-in chr and ord functions. If it is z, we replace it with a.

Here's the updated function:

Python

def character_frequency_encoding(word):

    next_string = ''

    for letter in word:

        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)

Solution Building: Step 2 - Counting the frequency of characters in next_string

The next step is to track the frequency of each character in next_string. We start by initializing an empty dictionary, frequency_dict. Then, we iterate over next_string. 
If the current character exists in frequency_dict, we increment its frequency by 1. If it doesn't exist, we add it to frequency_dict with a frequency of 1.

Incorporating this step into the function, our code now looks like this:

Python

def character_frequency_encoding(word):

    next_string = ''

    for letter in word:

        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)

    frequency_dict = {}

    for letter in next_string:

        if letter in frequency_dict:

            frequency_dict[letter] += 1

        else:

            frequency_dict[letter] = 1

Solution Building: Step 3 - Building the product list

Next, we calculate the numerical representation for each unique character. We initialize an empty list, combined_values, to store these numbers. 
For each character in frequency_dict, we calculate the product of its ASCII representation and its frequency in next_string and append this to combined_values.

Here's the updated function:

Python

def character_frequency_encoding(word):

    next_string = ''

    for letter in word:

        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)

    frequency_dict = {}

    for letter in next_string:

        if letter in frequency_dict:

            frequency_dict[letter] += 1

        else:

            frequency_dict[letter] = 1

    combined_values = []

    for letter, freq in frequency_dict.items():

        combined_values.append(ord(letter) * freq)

Solution Building: Step 4 - Sorting the final values

The final step is to sort the list combined_values in descending order. We use Python's built-in sort function. Here's our complete function:

Python

def character_frequency_encoding(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)
    frequency_dict = {}
    for letter in next_string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    combined_values = []
    for letter, freq in frequency_dict.items():
        combined_values.append(ord(letter) * freq)
    combined_values.sort(reverse=True)
    return combined_values

Lesson Summary

Well done! You've successfully tackled an intricate problem which required you to exercise multiple topics such as string manipulation, dictionary processing, and list sorting. 
This task underscored the importance of reusing already calculated values. I encourage you to apply what you've learned today to other tasks. 
There are many more exciting challenges wait'''

def character_frequency_encoding(word):
    next_string = ''
    for letter in word:
        next_string += 'a' if letter == 'z' else chr(ord(letter) + 1)
    frequency_dict = {}
    for letter in next_string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    combined_values = []
    for letter, freq in frequency_dict.items():
        combined_values.append(ord(letter) * freq)
    combined_values.sort(reverse=True)
    return combined_values

''' Exercise 1

Mike is fascinated by numbers and operations, having devised a unique number encoding scheme. Given an array numbers consisting of n integers, where n ranges from 11 to 100100 inclusive, 
Mike undertakes the following operations:

    For each number in the array that is not a multiple of 10, he increases it by 11.
    For each number that is a multiple of 1010, he assigns it a value of 11.

Following these operations, Mike calculates the frequency of each number in the new array. Subsequently, he establishes an association between each number and its frequency. 
This association maps the number to a product, defined as the multiplication of the number itself by its frequency.

Your task is to generate a list that encompasses these products, organized in ascending order. Each number in the array numbers spans from −100 to 100, inclusive.

For example, given the input array numbers = [5, 10, 15, 10, 5, 15], after applying Mike's operations, we have a resulting array of [6, 1, 16, 1, 6, 16]. 
The frequency of each number is 6: 2, 1: 2, 16: 2. The corresponding products (number * frequency) are 6*2 = 12, 1*2 = 2, and 16*2 = 32. 
Therefore, the output is [2, 12, 32], sorted in ascending order.
'''

def mike_number_encoding(numbers):
    frequency_dict = {}
    products_array = []

    operations = [] # Initialize an empty list and adjust numbers in the array - number + 1 if not a multiple of 10, or 1 if it is a multiple of 10
    for number in numbers:
        if number % 10 == 0:
            operations.append(1)
        else:
            operations.append(number + 1)

    # Create frequency dictionary
    for number in operations:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1


    for key, value in frequency_dict.items():
        products_array.append(key * value)

    products_array.sort()  # Sort the products in ascending order
    return products_array

numbers = [5, 10, 15, 10, 5, 15]
print(mike_number_encoding(numbers))  # Output: [2, 12, 32]

''' Exercise 2

You are provided with a string of n lowercase English characters, where n ranges from 1 to 500 inclusive. 
Your task is to return a dictionary where each key-value pair represents a letter k and its corresponding numerical representation v.

The numerical representation v of each character k is computed as follows: replace k with the character that comes three characters before it in the alphabetical order 
(wrap around to z when this is less than a), then multiply the ASCII value of the new character by the frequency of k in the provided string.

Your function should return a dictionary of the letters in the string and their corresponding numerical representations, sorted in ascending order by the characters.

Each character's ASCII value can be obtained using Python's built-in ord function, and the character corresponding to an ASCII value can be obtained using the chr function.

The returned dictionary should be in the format:

Python

{'character': numerical_representation}

For example, given the string 'abc', your function should return:

Python

{'a': 120, 'b': 121, 'c': 122}

In this case, we replace 'a' with 'x' and multiply its ASCII value (120) by its frequency (1) to get 120. For 'b', we replace it with 'y' and multiply its ASCII value (121) 
by its frequency (1) to get 121. And for 'c', we replace it with 'z' and multiply its ASCII value (122) by its frequency (1) to get 122. 

Then, we sort them based on the characters.'''

def character_numerical_representation(s):
    frequency_dict = {}
    adjusted_dict = {}

    for char in s:
        if char < 'd':
            new_char = chr(ord(char) + 23)
        else:
            new_char = chr(ord(char) - 3)
        
        if new_char in frequency_dict:
            frequency_dict[new_char] += 1
        else:
            frequency_dict[new_char] = 1
        

    for key, value in frequency_dict.items():
        # adjust keys back to original characters
        if key > 'w':
            adjusted_key = chr(ord(key) - 23)
        else:
            adjusted_key = chr(ord(key) + 3)
        adjusted_dict[adjusted_key] = ord(key) * value

    return dict(sorted(adjusted_dict.items()))

print(character_numerical_representation('abc'))  # Output: {'a': 120, 'b': 121, 'c': 122}
print(character_numerical_representation('xyz'))  # Output: {'x': 117, 'y': 118, 'z': 119}

''' Exercise 3
Bob, Alice's friend, is also interested in string manipulations. Inspired by Alice's technique, he has devised his own string encoding scheme. He takes a sentence, 
which is a string of n alphanumeric characters (ranging from a-z, A-Z, 0-9), including spaces and punctuation marks, with n ranging from 1 to 500, inclusive. 
His encoding technique consists of the following steps:

    He replaces each alphanumeric character with the previous character in their respective sequence, i.e., for alphabets, he moves in the alphabetical order, and for numbers, 
    he moves in the ordinal sequence.
        For instance, given a string word, for each character, if it's not a or A or 0, he replaces it with the character that precedes it in the sequence.
        For the character a or A, he replaces it with z or Z, respectively.
        For the number 0, he replaces it with 9.

    Another important aspect of Bob's algorithm involves frequency analysis. After shifting the characters, he counts the frequency of each alphanumeric character in the new string. 
    Then, he creates an association between each alphanumeric character and its frequency and ASCII value. 
    Each character maps to a number, which is the difference between the ASCII value of the character and its frequency. 
    Once this is done, he computes the absolute value of each of these differences.

The task is to help Bob generate a list of these absolute differences, sorted in ascending order.'''

def bob_string_encoding(sentence):

    frequency_dict = {}
    absolute_diff = []

    for char in sentence:
        #print(f"Working on {char} in {sentence}")
        if char.isalnum():
            #print(f"{char} passes the alpha numeric screen")
            # do some shit
            if char == 'a':
                new_char = 'z'
            elif char == 'A':
                new_char = 'Z'
            elif char == '0':
                new_char = '9'
            else:
                new_char = chr(ord(char) - 1)


            if new_char in frequency_dict:
                frequency_dict[new_char] += 1
            else:
                frequency_dict[new_char] = 1

    for key, value in frequency_dict.items():
        absolute_diff.append(ord(key) - value)
        #print(f"{key}, {value}: {ord(key)} - {value}")

    for diff in absolute_diff:
        if diff < 0:
            diff = -1 * diff
    
    absolute_diff.sort()
    return absolute_diff

    
sample = "Hello, 123!"
print(bob_string_encoding(sample))