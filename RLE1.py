'''
In this task, you are to write a Python function that implements the concept of Run-Length Encoding (RLE) on an alphanumeric input string. 
Run-length encoding is a simple form of data compression where sequences of data entities that are the same are stored as a single data entity along with its count. 
Each count must immediately follow the character it is associated with.

Your function's name should be encode_rle. It takes a string as an input argument and returns a new string that represents the input's run-length encoding.

Your function should operate only on alphanumeric characters (numbers 0-9 and uppercase and lowercase letters A-Z, a-z). 
For any other types of characters in the string, simply ignore them and do not include them in the final encoded output.

For instance, if the input string is "aaabbcccdde", the output should be "a3b2c3d2e1". 
If the input string includes non-alphanumeric characters, such as "aaa@@bb!!c#d**e", the output should be "a3b2c1d1e1".

We assume that the given input string could have up to 500 characters.
'''

def encode_rle(s):
    groups = []
    groups_str = ""
    current_group_char = None
    current_group_length = 0


    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_group_char:
                current_group_length += 1

            else:
                if current_group_char is not None:
                    groups.extend([current_group_char, current_group_length])
                current_group_char = char
                current_group_length = 1

    if current_group_char is not None:
        groups.extend([current_group_char, current_group_length])
    
    groups = str(groups)
    for i in groups:
        if i.isdigit() or i.isalpha():
            groups_str += i

    return groups_str

string_test = "aaa@@bb!!c#d**e"

print(encode_rle(string_test))  # Expected output: 'a3b2c1d1e1'