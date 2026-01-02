def solution(n):
    product = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            if product == 0:
                product += digit
            else:
                product *= digit
        n = n//10
    return product


'''
Your task is to construct a function that accepts an integer n and returns the integer with the same digits as n, but in reverse order. You should implement your solution using a while loop.

For instance, if the input is 12345, the output should be 54321.

Keep in mind that n will always be a positive integer between 11 and 108108.

Do not use built-in functions that convert the integer to another data type, such as a string, to reverse it. Solve the problem purely using mathematical operations and loop constructs.

Note that when the result has leading zeros, you should consider only the integer value (e.g., 1230 becomes 321 after the operation).
'''

def reverse_integer(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number

print(reverse_integer(467809))
print(reverse_integer(98934000))
