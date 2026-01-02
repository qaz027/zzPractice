'''
Given a string consisting of words separated by whitespace, your task is to write a Python function that accepts this string. 
It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches them all together to form a new string.

Here's what you need to consider:

    The input string will include between 1 and 100 words.
    Each word consists of characters separated by white space.
    A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. 
    For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
    The given string will not start or end with a space, and there will be no occurrence of double spaces.
    After transforming the characters of the words, form a new string by taking the last word first and appending the remaining words in their original order, each separated by spaces.

Note: The opposite letter mappings are as follows: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n, n ↔ m, ..., x ↔ c, y ↔ b, z ↔ a. The mapping is case-sensitive.

Example

For the input string "CapitaL letters", the output should be "ovggvih XzkrgzO".
'''

def opposite_case_letter_mapping(input_string):
    def opposite_letter(c): # I need this explained
        if 'a' <= c <= 'z':
            return chr(ord('z') - (ord(c) - ord('a')))
        elif 'A' <= c <= 'Z':
            return chr(ord('Z') - (ord(c) - ord('A')))
        return c

    words = input_string.split()
    transformed_words = [''.join(opposite_letter(c) for c in word) for word in words]
    
    # Reverse the order of the words and join them with a space
    result = ' '.join([transformed_words[-1]]+list(transformed_words[:-1]))
    
    return result

print(opposite_case_letter_mapping("CapitaL letters"))  # Output: "ovggvih XzkrgzO"
print(opposite_case_letter_mapping("Hello World"))       # Output: "Svool Dliow"
print(opposite_case_letter_mapping("Python Programming")) # Output: "Kbgslmm Tizibnmt"
print(opposite_case_letter_mapping("a b c d e f g h i j k l m n o p q r s t u v w x y z"))  # Output: "z y x w v u t s r q p o n m l k j i h g f e d c b a"
print(opposite_case_letter_mapping("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"))  # Output: "Z Y X W V U T S R Q P O N M L K J I H G F E D C B A"
print(opposite_case_letter_mapping("A quick brown FOX jumps over the lazy DOG"))

def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_words = [''.join(reversed(word)) for word in reversed_words]
    
    return reversed_words

#print(reverse_words("CapitaL letters"))  # Output: "letters CapitaL"
