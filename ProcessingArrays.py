'''Lesson

Task Statement

Our mission for today is to generate a unique encoded message for a book club. 
Here's the fun part: to create a cryptic message, we will process a string and an array of numbers simultaneously and stop once a given condition is satisfied.

For the string, our task is to replace each letter with the next alphabetical letter and then reverse the entire updated string. For the array of numbers, 
our task is to divide each number by 2, round the result, and accumulate the rounded numbers until their total exceeds 20.

When the accumulated total exceeds 20, we immediately stop the process and return the updated string and the as yet unprocessed numbers in their original order.

Example

Consider the input string "books" and array [10, 20, 30, 50, 100].

We start our process with an empty string and a sum of 0.

    For the first character 'b' in 'books', we replace it with the next alphabet 'c'. For the corresponding number 10 in the array, we divide it by 2 and round it. 
    The result is 5. The sum after first operation is 5 which is less than 20, so we continue to the next character.
    For the next character 'o', we replace it with 'p'. And for the corresponding number 20 in the array, half and rounded is 10. 
    The sum after the second operation is 15 (5 + 10). The sum still doesn't exceed 20, so we move to third character.
    For the next character 'o', we replace it with 'p'. And for the corresponding number 30 in the array, half and rounded is 15. 
    When we add this '15' to our previously calculated sum 15, it totals to 30 which is more than 20. So, we stop the process here.
    We have processed 'b', 'o', and 'o' from the word 'books' and replaced them with 'c', 'p', and 'p' respectively to get "cpp". After reversing, we get "ppc".
    For the array, we exclude any numbers that we have processed. Hence, we exclude the first three numbers and the array becomes [50, 100].

So the output should be ('ppc', [50, 100]).

Solution Building: Step 1 - String and Array Initialization
Let's begin our journey by setting up two crucial components: our resultant string and a variable to keep track of the cumulative sum.


Solution Building: Step 2 - Iteration and Updates
With the setup complete, it's time to roll up our sleeves and process the string and array. 
We need to iterate over the inputString and update each character to its next alphabetical character. 
Simultaneously, we'll keep tabs on our array condition - if the sum of half of the numbers crosses our threshold of 20, we should stop the process.


Solution Building: Step 3 - Final Touch Up and Return

With the updates complete, we're one step away from solving this mystery. 
We must reverse our string to generate the final encoded message! At the end, we return the processed string and the remaining array.

'''

def lesson_solution(inputString, numbers):
    result = ''
    sum_so_far = 0
    i = 0
    while i < len(inputString) and sum_so_far <= 20:
        result += 'a' if inputString[i] == 'z' else chr(ord(inputString[i]) + 1)
        half_number = round(numbers[i] / 2)
        sum_so_far += half_number
        i += 1
    return result[::-1], numbers[i:]

''' Exercise 1

As an aspiring musician, you are given a chance to create a unique encrypted song. The song's lyrics will be encoded based on specific rules applied to an array of integers and a string.

You are provided with an array of n integers, where n is between 1 to 500, inclusive. Each integer in the array ranges from −100 to 100, inclusive. 
Accompanying this, you are presented with a string comprising n lowercase alphabetical characters.

Here are your tasks:

    For the array, calculate the absolute value of each number and multiply it by 2. Accumulate these results until the total exceeds 100.

    For the string, your task is to replace each letter with the preceding alphabetical character and then concatenate these characters in the order they were processed. 
    However, if the current character in the string is a vowel (i.e., 'a', 'e', 'i', 'o', 'u'), it should not be processed, and you should stop the process immediately.

When the accumulated total exceeds 100, or if the next character is a vowel, halt the process and return the transformed string and the remainder of the array in their original order.

Your main challenge here is to process the given string and integer array according to the stated rules but stopping when a certain condition is met. 
The final output should be a tuple with the transformed string as the first element and the remaining, unprocessed part of the array as the second element.

'''

def encrypted_song(numbers, string):
    i = 0
    total = 0
    
    transformed_string = ''

    while total < 100 and i < len(string):
        num = 0
        
        if string[i] in 'aeiou':
            break

        transformed_string += 'z' if string[i] == 'a' else chr(ord(string[i]) - 1)

        if numbers[i] > 0:
            num = numbers[i]
        else:
            num = numbers[i] * -1
        
        total += 2*num
        i += 1
        

    return (transformed_string, numbers[i:])

string, numbers = 'abcdef', [10, 20, 30, 40, 50, 60]

#print(encrypted_song(numbers,string))

''' Exercise 2

You are given a string of length at most 100 and an array of at most 100100 integers. The task requires you to process both the string and the array simultaneously from 
their first elements, and continue as long as certain condition on the array is satisfied. Return the modified string and certain portion of the original array.

For the string, your goal is to replace every occurrence of a vowel with the next vowel in the sequence, wrapping around from 'u' to 'a'. If the character is a consonant, 
it should be replaced with the next consonant in alphabetical order, wrapping around from 'z' to 'b'.

Meanwhile, for the array of integers, you are instructed to multiply each integer by 3 and add the result to a total until that total reaches or exceeds 100. 
Each integer in the array can range from −50 to 50, inclusive.

Finally, return the modified string and any unprocessed integers from the array in their original order.

Stop processing when the total sum, restricted to 100100, is met or when all elements have been processed. In other words, process both the string and the array 
while the condition holds true.

If you process all elements in the array and the string, and the total sum still has not reached 100100, simply return the processed string and an empty list.

Consider using Python's built-in functions such as ord(), chr(), and round() to aid in achieving this.

The final return format should be a tuple containing the modified string and the list of unprocessed integers.

Example:

Input:

    String: "examplestring"
    Array: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Start processing both the string and the array:

    Character 'e' and Number 1:
        'e' is a vowel, so it is replaced with the next vowel 'i'.
        The array calculation: 1 · 3 = 3, total = 3.

    Character 'x' and Number 2:
        'x' is a consonant, so it is replaced with the next consonant 'y'.
        The array calculation: 2 · 3 = 6, total = 9.

    Character 'a' and Number 3:
        'a' is a vowel, so it is replaced with the next vowel 'e'.
        The array calculation: 3 · 3 = 9, total = 18.

    Character 'm' and Number 4:
        'm' is a consonant, so it is replaced with the next consonant 'n'.
        The array calculation: 4 · 3 = 12, total = 30.

    Character 'p' and Number 5:
        'p' is a consonant, so it is replaced with the next consonant 'q'.
        The array calculation: 5 · 3 = 15, total = 45.

    Character 'l' and Number 6:
        'l' is a consonant, so it is replaced with the next consonant 'm'.
        The array calculation: 6 · 3 = 18, total = 63.

    Character 'e' and Number 7:
        'e' is a vowel, so it is replaced with the next vowel 'i'.
        The array calculation: 7 · 3 = 21, total = 84.

    Character 's' and Number 8:
        's' is a consonant, so it is replaced with the next consonant 't'.
        The array calculation: 8 · 3 = 24, total = 108 (stop, as total reached over 100).

The rest of the string and array processing stops since the total has exceeded 100.

Output:

    Resulting string: "iyenqmit"
    Remaining array: {9, 10}

In conclusion:

    Processed String: The string "examplestring" becomes "iyenqmit".
    Processed Array: With multiplications and additions up to the total exceeding 100, the processed numbers are [1, 2, 3, 4, 5, 6, 7, 8] and the remaining array is {9, 10}.
'''

def process_string_array(inputString, numbers):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    total = 0
    mod_string = ''
    i = 0

    while total < 100:
        if total < 100 and i >= len(numbers):
            return (mod_string, [])
            
        if i >= len(inputString):
            break
        #print(f"Input String: {inputString}\ni: {i}\nTotal: {total}\nCurrent letter to adjust: {inputString[i]}")
        total += numbers[i] * 3

        if inputString[i] in vowels:
            #print(f'{inputString[i]} is in the vowels string')
            if inputString[i] == 'u':
                #print(f"{inputString[i]} is identified as 'u'")
                mod_string += 'a'
                #print(f"Added 'a' to the mod_string")
                #print(f"Mod string: {mod_string}")
            # return the vowels index and add 1
            else:
                idx = vowels.index(inputString[i])
                # iterate to the next vowel and append to mod_string
                mod_string += vowels[idx + 1]
                #print(f"Added {vowels[idx + 1]} to the mod_string")
                #print(f"Mod string: {mod_string}")

        elif inputString[i] in consonants:
            #print(f'{inputString[i]} is in the consonants string')
            idx = consonants.index(inputString[i])
            # iterate to the next constanant and append to mod_string
            if inputString[i] == 'z':
                #print(f"{inputString[i]} is identified as 'z'")
                mod_string += 'b'
            else:
                mod_string += consonants[consonants.index(inputString[i])+1]

        i += 1

    return (mod_string, numbers[i:])

input_string = 'abcdefghijk'
array = [5,10]
print(process_string_array(input_string,array))

def process_string_array_submitted(inputString, numbers):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    total = 0
    mod_string = ''
    i = 0

    while total < 100:
        if total < 100 and i >= len(numbers):
            return (mod_string, [])
            
        if i >= len(inputString):
            break

        total += numbers[i] * 3

        if inputString[i] in vowels:
            if inputString[i] == 'u':
                mod_string += 'a'
            else:
                mod_string += vowels[vowels.index(inputString[i]) + 1]

        elif inputString[i] in consonants:
            if inputString[i] == 'z':
                mod_string += 'b'
            else:
                mod_string += consonants[consonants.index(inputString[i])+1]

        i += 1

    return (mod_string, numbers[i:])


''' Exercise 2
You are required to create a function that, given two parameters — an array of integers and a string — will return a modified text message based on these elements.

You will be provided with an array of n integers, where n is between 1 and 100, inclusive, and a string with m characters, where m ranges from 1 to 500, inclusive. 
Each element in the array will range from −100 to 100, inclusive.

Your initial task is to process the array by subtracting 3 from each number and then accumulating the absolute values of each number until their total exceeds 30. 
If the total exceeds 30, you must stop processing the array immediately.

Concurrently, you must process the given string. In this part, replace each lowercase character in your string with the succeeding alphabetical character in a cyclic manner; 
for instance, 'a' should be replaced by 'b', 'b' should be replaced by 'c', and so on, until 'z', which should be replaced by 'a'. 
If a character is not a lowercase letter, it should be left as is.

Similar to the array, if the total absolute value from the array operations crosses the threshold of 30, you should cease the string modification immediately.

At the conclusion, return both an updated string with all processed characters and the remaining, unprocessed portion of the initial array, respectively.

Can you create a function that accomplishes all this?'''

def return_text_message(arr, text):

    total = arr[0] - 3
    if total < 0:
        total = total * -1
    abs_diff = 0
    i = 0
    msg = ''

    while total < 30:
        if text[i].islower():
            if text[i] == 'z':
                msg += 'z'
            else:
                msg += chr(ord(text[i])+1)
        else:
            msg += text[i]
        
        i+= 1
        
        abs_diff = arr[i] - 3
        if abs_diff < 0:
            abs_diff = abs_diff * -1
        
        total += abs_diff


    return (msg, arr[i:])

array = [5, 10, 15, 20, 25]
string = "hello world"

#array = [-5, -10, -15, -20, -25]
#string = "python is fun"

print(return_text_message(array, string))