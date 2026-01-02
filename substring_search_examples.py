''' Leson
Task Statement and Description

Here's our challenge: we have two lists of strings of the same length, one containing the "original" strings and the other, the "substrings". We're to identify all occurrences of each substring within its corresponding original string and return a list of the starting indices of these occurrences. Remember, index counting should start from 0.

Example

If we take the following lists: Original List: ["HelloWorld", "LearningPython", "GoForBroke", "BackToBasics"] Substring List: ["loW", "ear", "o", "Ba"].

This will produce the following outputs: In "HelloWorld", "loW" starts at index 3. In "LearningPython", "ear" starts at index 1. In "GoForBroke", "o" appears at indices 1, 3, and 7. In "BackToBasics", "Ba" starts at indices 0 and 6.

So, if findSubString(["HelloWorld", "LearningPython", "GoForBroke", "BackToBasics"], ["loW", "ear", "o", "Ba"]) is called, the function should return

[
    "The substring 'loW' was found in the original string 'HelloWorld' at position(s) 3.",
    "The substring 'ear' was found in the original string 'LearningPython' at position(s) 1.",
    "The substring 'o' was found in the original string 'GoForBroke' at position(s) 1, 3, 7.",
    "The substring 'Ba' was found in the original string 'BackToBasics' at position(s) 0, 6."
]

The Final Solution

Here is the comprehensive solution, which incorporates all the steps above:
'''

def substr_solution(orig_strs, substrs):
    result_arr = []

    for original, substring in zip(orig_strs, substrs):
        start_pos = original.find(substring)
        match_indices = []
        while start_pos != -1:
            match_indices.append(str(start_pos))
            start_pos = original.find(substring, start_pos + 1)
        result_arr.append(f"The substring '{substring}' was found in the original string '{original}' at position(s) {', '.join(match_indices)}.")

    return result_arr


''' Example 1

Imagine you are working on a new feature for a text processing application. The feature requires you to provide users with the option to replace all occurrences of a certain substring in the entered text with a new substring.

You are tasked with writing a function, replace_substring(text: str, old: str, new: str) -> str, that does the following:

    Accepts as input text (a string of length n, where 1 ≤ n ≤ 500, which includes only lowercase alphabets and spaces), 
    old (a string of length k, where 1 ≤ k ≤ n, which includes only lowercase alphabets), 
    and new (a string of length m, where 1 ≤ m ≤ 500, which includes only lowercase alphabets).

    Replaces every occurrence of the string old in text with the string new.

    Returns the updated text string with all replaced substrings.

Please ensure that the case of the letters remains consistent during the process, meaning an uppercase letter should be replaced with an uppercase letter, and a lowercase letter should be replaced with a lowercase one.

replace_substring("hello world", "world", "friend")
"hello friend"
'''

print("Hello World".replace("World", "Friend"))  # Example of string replacement

def replace_substring(text, old, new):
    return text.replace(old, new)

''' Exercise 2

You are given two lists, sentences and words, each comprising n strings, where n ranges from 11 to 100100 inclusive. 
Each string in the sentences list has a length ranging from 11 to 500500 inclusive. 
Each word in the words list is a single lowercase English alphabet word of length 11 to 1010 inclusive.

Your task is to find all instances of each word in the corresponding sentence from the sentences list and replace them with the reverse of the word.
The words and sentences at the same index in their respective lists are deemed to correspond to each other.

Return a new list comprising n strings, where each string is the sentence from the sentences list at the corresponding index, with all instances of the word from the words list at the same index replaced with its reverse.

If the word is not found in the respective sentence, keep the sentence as it is.
Remember, while replacing the instances of word in the sentence, you should preserve the case of the initial letter of the word. 
If a word starts with a capital letter in the sentence, its reversed form should also start with a capital letter.

Example

For sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'] and words = ['simple', 'bond', 'e'], 
the output should be ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'].
'''

def reverse_solution(sentences, words):
    result = []

    for sentence, word in zip(sentences, words):
        reversed_word = word[::-1]
        if sentence.lower().count(word.lower()) > 0:
            # Preserve the case of the first letter
            if word[0].isupper():
                reversed_word = reversed_word.capitalize()
            else:
                reversed_word = reversed_word.lower()
            modified_sentence = sentence.replace(word, reversed_word)
            modified_sentence = modified_sentence.replace(word.capitalize(), reversed_word.capitalize())
            result.append(modified_sentence)
        else:
            result.append(sentence)

    return result

sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'] 
words = ['simple', 'bond', 'e']

print(reverse_solution(sentences, words))  # Output: ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e']


''' Exercise 3

Humans often make mistakes when they are typing quickly. In some cases, they may press two keys simultaneously, resulting in swapped characters in the text. 
Your task is to craft a Python function that helps identify such typos. Specifically, you are asked to construct a function called spot_swaps(source: str, target: str) -> List[Tuple[int, str, str]] that behaves as follows:

Given two strings, source and target, of the same length n (1 ≤ n ≤ 500), inclusive, both comprise only lowercase English letters. 
The function should return a list of tuples. Each tuple should contain three elements: the zero-based index of the swap in the source string, the character (a string of length 1) 
at that index in source, and the character that swapped places with the source character in target.

In other words, go over both strings simultaneously and, for each character from source and target at position i, find situations when source[i] != target[i] and source[i+1] = target[i] and source[i] = target[i+1]. 
This implies that the characters at positions i and i+1 in the source string swapped places in the target string.

Note:

    Characters can be swapped at most once.
    The swapped character pairs should be returned in a list in the order they were found (from the string start to end).
    Don't check for swaps at the last position of a string, since there is no character with which to swap.

Example

For source = "hello" and target = "hlelo", the output should be [(1, 'e', 'l')].'''

def spot_swaps(source: str, target: str) -> list:
    swapped = []

    for i in range(len(source) - 1):
        if source[i] != target[i] and source[i+1] == target[i] and source[i] == target[i+1]:
            swapped.append((i, source[i], target[i]))

    return swapped

source = "hello"
target = "hlelo"
print(spot_swaps(source, target))  # Output: [(1, 'e', 'l')]

''' Exercise 4

You are given two lists: sourceArray and searchArray, consisting of n and m tuples respectively, where n is an integer such that 1 ≤ n ≤ 100 and 
m is an integer such that 1 ≤ m ≤ 500. Each tuple in both arrays contains two elements: an integer identifier and a string. 
The identifiers in both arrays range from 1 to 100, inclusive. The strings in sourceArray consist of alphanumeric characters with lengths ranging from 1 to 100, inclusive. 
The strings in searchArray have lengths ranging from 1 to 500, inclusive.

Your task is to implement a function stringSearch(sourceArray, searchArray) that takes these two arrays as input and returns an array that includes all tuples from sourceArray 
for which its string is a substring of at least one string in any tuple from searchArray and the identifier of the source tuple is less than or equal to the identifier of the 
search tuple.

The order in which the tuples appear in the result should reflect their original order in the sourceArray. If no matches are found, the function should return an empty array.

For example, if sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')] and searchArray = [(1, 'abcdef'), (5, 'uvwxy')], the function should return [(1, 'abc')] since 
'abc' and 'def' are substrings found in 'abcdef', but 'def' is associated with 2 in sourceArray which is not less than or equal to 1 in searchArray. 
The string 'xyz' is not found in either 'abcdef' or 'uvwxy', so it is not included in the result.

This task requires mastery of skills in nested looping and array manipulation, especially in the context of searching for a string within other strings.'''

def searchString(sourceArray, searchArray):
    result = []

    for id, source_str in sourceArray:
        for search_id, ref_str in searchArray:
            if source_str in ref_str and id <= search_id:
                result.append((id, source_str))
                break


    return result

sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')] 
searchArray = [(1, 'abcdef'), (5, 'uvwxy')]

print(searchString(sourceArray, searchArray))  # Output: [(1, 'abc')]

''' Exercise 5

You are given two lists of integers (listA and listB), each containing n elements, with n ranging from 1 to 50. 
Each element in both lists can range from -1000 to 1000, inclusive.

Your task is to write a Python function that identifies pairs of integers {a, b} wherein a belongs to listA and b belongs to listB, and a is greater than b. 
The function should return all such pairs in the order in which a appears in listA.

For instance, if listA consists of [5, 1, 8, -2, 0] and listB comprises [3, 2, 7, 10, -1], 
the output should be [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)].

Importantly, the order of elements in the output tuples should reflect the sequence in which a appears in listA. 
A pair cannot be included more than once. If no pair meets the condition, the function should return an empty list.

Hint: Solving this task requires the use of nested loops. The outer loop should iterate through listA and the inner loop through listB, 
checking the condition a > b during each iteration.'''

def find_pairs(listA, listB):
    pairs = []

    for a in listA:
        for b in listB:
            if a > b:
                if (a, b) not in pairs:
                    pairs.append((a,b))

    return pairs

listA = [1000]*50
listB = [-1000]*50

print(find_pairs(listA, listB))  # Output: [(1000, -1000)]

''' Exercise 6

You will be given two arrays of integers. The first array has n elements, and the second array has k elements. Sizes n and k both range from 1 to 100, inclusive. 
The elements of both arrays can fall within a range of -100 to 100, inclusive.

Your task is to write a Python function that will locate and return an array of all pairs of integers with the property that the first element of each pair comes 
from the first array and the second element of each pair comes from the second array, such that the sum of the two elements of the pair is a perfect square. 
A perfect square, as you know, is an integer that is the square of another integer.

The order of pairs in your output should correspond to the order of the elements in the input arrays. For example, if the two arrays are [2, 3, 16] and [1, 9, 10], 
the function should return [(3, 1), (16, 9)] because 3+1=4 (which is the square of 2) and 16+9=25 (which is the square of 5).

If no such pairs exist, or if either input array is empty, your function should return an empty list.'''

def sum_is_perfectSquare(array1, array2):
    pairs = []

    for a in array1:
        for b in array2:
            total = a + b

            # if total is perfect square - append to pairs
            if total >= 0:  # Only check for perfect squares for non-negative totals
                root = int(total**0.5)
                if root * root == total:
                    pairs.append((a, b))

    return pairs
