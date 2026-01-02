'''
You are given a string s of length n, with n ranging from 1 to 500 inclusive. This string represents the complex and jumbled record of a sports game. It combines player names and scores but lacks a uniform structure. The player names consist of words made up of lowercase English alphabets (a-z), while the scores are integers ranging from 1 to 100 inclusive.

Your mission involves writing a Python function solution(). This function should parse the given string, isolate the integers representing player scores, and return the sum of these scores.

For instance, for the input string, "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe", your function should return the sum 5 + 10 + 2 + 1, which totals 18.'''

def solution(input_string):
    import re
    s = input_string.strip()
    # Use regex to find all integers in the string
    scores = re.findall(r'\b\d+\b', s)
    # Convert found strings to integers and sum them up
    total_score = sum(int(score) for score in scores)
    print(total_score)


def solution2(input_string):
    numbers = []
    hold = ''
    sum = 0
    prev_char_digit = 0
    prev_char = ''
    digit_length = 0
    for char in ",?.;":
        input_string = input_string.replace(char, '' )
        print(input_string)
    words = input_string.split()
    for word in words:
        print(word)
        if word.isdigit():
            numbers.append(int(word))
            print(f"{word} is a digit, added to numbers list.")
            print(f"Current numbers list: {numbers}")
        else:
            # scan through each character in the word for digits
            for char in word: 
                
                print(f"Processing character: {char} in word: {word}")
                if char.isdigit():
                    print(f"{char} is a digit.")
                    hold += char
                    digit_length += 1
                    # prev_char = char
                    prev_char_digit = 1
                    print(f'{prev_char} is the previous character, prev_char_digit status is {prev_char_digit}, hold is now {hold}.')
                
                elif char.isalpha() and prev_char_digit:
                    print(f"{char} is a letter after a digit {prev_char}.")
                    numbers.append(int(hold))
                    print(f"{hold} is a digit, added to numbers list.")
                    hold = ''
                    prev_char_digit = 0
                    digit_length = 0
                    prev_char = char
                    print(f"Current numbers list: {numbers}")
                prev_char = char

    for each in numbers:
        sum += each

    return sum

input_string = "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"
input_string = "jake scored1point, john scored21points"
print(solution2(input_string))  # Output: 18

#print(solution(input_string))

def solution(input_string):
    numbers = []
    hold = ''
    sum = 0
    prev_char_digit = 0
    prev_char = ''
    digit_length = 0
    for char in ",?.;":
        input_string = input_string.replace(char, '' )
        #print(input_string)
    words = input_string.split()
    for word in words:
        
        #print(word)
        if word.isdigit():
            numbers.append(int(word))
            #print(f"{word} is a digit, added to numbers list.")
            #print(f"Current numbers list: {numbers}")
        else:
            # scan through each character in the word for digits
            for char in word: 
                
                #print(f"Processing character: {char} in word: {word}")
                if char.isdigit():
                    #print(f"{char} is a digit.")
                    hold += char
                    digit_length += 1
                    # prev_char = char
                    prev_char_digit = 1
                    #print(f'{prev_char} is the previous character, prev_char_digit status is {prev_char_digit}, hold is now {hold}.')
                
                elif char.isalpha() and prev_char_digit:
                    #print(f"{char} is a letter after a digit {prev_char}.")
                    numbers.append(int(hold))
                    #print(f"{hold} is a digit, added to numbers list.")
                    hold = ''
                    prev_char_digit = 0
                    digit_length = 0
                    prev_char = char
                    #print(f"Current numbers list: {numbers}")
                prev_char = char

    for each in numbers:
        sum += each

    return sum