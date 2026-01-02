'''
In this task, you need to write a Python function that finds repeating two-character patterns in a string. 
The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.

The function should return a new string that lists each pair followed by the number of times it repeats consecutively. 
For example, let's break down the input string "aaabbabbababacab":

    Divide the string into pairs:
        "aa"
        "ab"
        "ba"
        "bb"
        "ab"
        "ab"
        "ac"
        "ab"

    Note the consecutive pairs:
        "ab" appears twice consecutively in the middle.

    Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".

Similarly, for the input string "aaababbababaca", the output should be "aa1ab2ba3ca1".

Key points to remember:

    The input string always has an even number of characters.
    The string contains only lowercase letters.
    The string length can be up to 500 characters.

Focus on finding consecutive repetitions of the same two-character patterns.'''

def find_repeating_pairs(s):
    if len(s) < 2 or len(s) % 2 != 0:
        return ""

    result = []
    count = 1
    previous_pair = s[0:2]

    for i in range(2, len(s), 2):
        current_pair = s[i:i+2]
        if current_pair == previous_pair:
            count += 1
        else:
            result.append(f"{previous_pair}{count}")
            previous_pair = current_pair
            count = 1

    # Append the last pair
    result.append(f"{previous_pair}{count}")

    return ''.join(result)

test_string1 = "aaabbabbababacab"
test_string2 = "aaababbababaca"

print(find_repeating_pairs(test_string1))  # Expected output: "aa1ab1ba1bb1ab2ac1ab1"
print(find_repeating_pairs(test_string2))  # Expected output: "aa1ab2ba3ca1"

print(find_repeating_pairs("aaabbabbababacab")) # Expected output: "aa1ab1ba1bb1ab2ac1ab1"