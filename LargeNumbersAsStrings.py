''' Lesson
Introduction

Hello and welcome! Today, we'll delve deep into a captivating problem that involves large numbers -- specifically, adding extraordinarily large numbers. 
As you may have noticed, traditional calculators and even some programming languages struggle when numbers get exceedingly large. 
To handle such scenarios efficiently, we'll simulate this process manually using strings. 
By the end of this discussion, you'll be able to add together numbers that have thousands or even tens of thousands of digits. Intriguing, right? Let's get started.

Task Statement
In today's task, we'll step into the world of large numbers, where, specifically, we are given two exceedingly large positive integers. 
However, these aren't your average, everyday large numbers. They are so vast they're represented as strings that can be up to 10,000 digits long!

Accepting our mission means writing a Python function that binds these two "string-numbers" together. 
The challenge is to perform the addition without converting the entire strings into integers.

Finally, our function should return the resulting sum, represented as a string. 
While it might seem daunting at first, don't worry -- we'll break it down step by step, mimicking how we manually add numbers.

Solution Building: Step 1

Before we start coding, let's consider the strategy we're going to adopt. 
You may recall that each digit in a number has a value, and the position of the digit determines its influence on the total value of the number. 
This system is called place-value notation.

The first step requires initialization of our variables. We'll use two indices, i and j, to point to the current digit in num1 and num2, respectively. 
We'll also need a variable carry to hold carryovers from each addition operation. 
Lastly, we'll employ a list named res to hold our result, where each digit from the addition is appended at the front.

Python
def solution(num1, num2):

    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []

    
Solution Building: Step 2

Having initialized our variables, we can advance to the next step, which involves scanning through num1 and num2 from right to left. 
This scanning goes from the least significant digit to the most significant one.

For each iteration, we extract the digits n1 from num1 and n2 from num2. 
If i or j is less than 0, we've processed all the digits in one of the numbers. Consequently, we consider these additional digits as 0.

Python

def solution(num1, num2):

    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []

    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0

Solution Building: Step 3

After obtaining the digits n1 and n2, our immediate step is to add them. However, the carry, which accumulates any overflow from the addition of previous column digits, 
must also be added. This sum results in a two-digit number, in which the tens place becomes a new carry and the units place is the resultant digit.

Subsequently, we append curr to res and decrement both i and j before embarking on the next iteration. 
Finally, we reverse res and join the digits into a single string to acquire our result.'''

def lesson_solution(num1, num2):
    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
    
    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        total = n1 + n2 + carry
        if total > 9:
           carry = 1
        else:
           carry = 0
        curr = total%10
        res.append(str(curr))
        i, j = i - 1, j - 1

    return ''.join(res[::-1])  # reverse the list and join into a single string



''' Exercise 1

For this task, you are given two non-negative integers, num1 and num2. 
However, these are not just ordinary numbers; they are so large that they should be represented as strings instead of normal integers. Each can be up to 100 digits long.

Your mission is to write a Python function that compares these two "string-numbers" without converting the entire strings into integers. 
Your function should determine whether num1 is greater than, less than, or equal to num2.

Your function can only use comparison operators (such as >, <, or ==) on strings. So “1” < “2” is allowed, but 1 < 2 is not. 
The task requires that you manually compare the two strings from the most significant digit to the least significant. 
You should implement your own logic to compare two string numbers.

The function should return the following results:

    If num1 is greater than num2, your function should return 1.
    If num2 is greater than num1, your function should return -1.
    If num1 and num2 are equal, your function should return 0.

Let's look at the following examples:

For `num1` = '12345' and `num2` = '1234', your function should return `1`.
For `num1` = '1234' and `num2` = '12345', your function should return `-1`.
For `num1` = '12345' and `num2` = '12345', your function should return `0`.

'''

def compare_large_numbers(num1, num2):
    # Compare lengths first
    if len(num1) > len(num2):
        return 1
    elif len(num1) < len(num2):
        return -1
    
    # If lengths are equal, compare digit by digit
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            return 1
        elif num1[i] < num2[i]:
            return -1
    
    # If all digits are equal
    return 0

#print(compare_large_numbers('12345', '1234'))   # Output: 1
#print(compare_large_numbers('1234', '12345'))   # Output: -1
#print(compare_large_numbers('12345', '12345'))   # Output: 0

''' Exercise 2

You are given two exceedingly large positive decimal numbers, num1 and num2, both represented as strings. 
The length of these strings can range anywhere from 1 to 500 characters. The challenge here is to subtract num2 from num1 without directly converting the strings into integers.

Create a Python function that performs this operation and returns the resultant string, referred to as num3.

Please note that the subtraction will not result in a negative number, as num1 will always be greater than or equal to num2.'''


''' This exercise is brutal - had me stumped for a while'''
def subtract_large_numbers(num1, num2):

    # Initialize variables
    i, j, borrow, res = len(num1) - 1, len(num2) - 1, 0, []
    count = 5
    num3 = 0

    while i >= 0 or j >= 0 or borrow > 0 and count > 0:
        print(f"i: {i}, j: {j}, borrow: {borrow}")
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        
        if borrow == 1:
            print(f"Adjusting n1: {n1} - 1 for borrow")
            n1 = int(n1 - 1)
            borrow = 0  # Reset borrow after adjustment
        # Adjust for borrow
        if int(n1 - n2 - borrow) < 0:
            print(f"n1: {n1}  n2: {n2}  borrow: {borrow}")
            print(f"n1 - n2 - borrow is negative: {n1-n2-borrow}")
            print(f"n1: {n1} is less than n2: {n2}")
            n1 += 10
            borrow = 1
            print(f"Borrowing, new n1: {n1}, borrow set to {borrow}")
        else:
            print(f"n1: {n1} is sufficient against n2: {n2}, no need to borrow")
            borrow = 0
        
        curr = n1 - n2
        res.append(str(curr))
        print(f"Current digit after subtraction: {curr}")
        print(f"Result so far: {''.join(res[::-1])}")
        
        i -= 1
        j -= 1
        count -= 1
        print(f"Next indices: i: {i}, j: {j}, count: {count}")
        num3 = int(''.join(res[::-1]))


    return str(num3)  # Reusing the solution function for addition as a placeholder

# Example usage
#print(subtract_large_numbers('21', '2'))  # Output: '199512'
#print(subtract_large_numbers('398746', '199234'))  # Output: '199512'

#print(subtract_large_numbers('10000', '9999'))  # Output: '1'

def solution(num1, num2):
    i, j, borrow, res, num3 = len(num1) - 1, len(num2) - 1, 0, [], 0
    
    #count = 2

    while i >= 0 or j >= 0 or borrow > 0: # and count > 0:
        #print(f"i: {i}, j: {j}, borrow: {borrow}")
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        
        if borrow == 1:
            #print(f"Adjusting n1: {n1} - 1 for borrow")
            n1 -= 1
            borrow = 0
        # Adjust for borrow
        if n1 < n2 + borrow:
            #print(f"n1: {n1} is less than n2: {n2}")
            n1 += 10
            borrow = 1
            #print(f"Borrowing, new n1: {n1}, borrow set to {borrow}")
        else:
            #print(f"n1: {n1} is sufficient, no need to borrow")
            borrow = 0
        
        curr = n1 - n2
        res.append(str(curr))
        num3 = int(''.join(res[::-1]))
        #print(f"Current digit after subtraction: {curr}")
        
        i -= 1
        j -= 1
        #count -= 1
        #print(f"Next indices: i: {i}, j: {j}, count: {count}")


    return str(num3)  # Reusing the solution function for addition as a placeholder

''' Exercise 3

You are tasked with writing a Python function to multiply two extremely large positive integers. 
These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. 
The challenging part is that you should perform the multiplication without converting the entire strings into integers.

Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, 
starting from the rightmost digits, and add the results after shifting appropriately.

Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, 
and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.

Challenge yourself, and Happy Coding!'''

# def multiply_large_numbers(num1, num2):
#     num3 = 0
#     i, j = len(num1) - 1, len(num2) - 1
#     carry = 0
#     res = []
#     while i >= 0 or j >= 0 or carry > 0:
#         n1 = int(num1[i]) if i >= 0 else 0
#         n2 = int(num2[j]) if j >= 0 else 0
        
#         product = n1 * n2 + carry
#         carry = product // 10
#         curr = product % 10
        
#         res.append(str(curr))
        
#         i -= 1
#         j -= 1
#         num3 = int(''.join(res[::-1]))  # Reverse the result list and

#     return str(num3)

# def multiply_large_numbers(num1, num2):
#     print()
#     print(f"Multiplying {num1} and {num2}")
#     num3 = 0
#     i, j = len(num1) - 1, len(num2) - 1
#     carry = 0
#     res = []
#     numbers_to_add = []
#     while i >= 0:
#         n1 = int(num1[i]) if i >= 0 else 0
#         print(f"Processing digit {n1} from num1 at index {i}")
#         multiply_n1_10 = 10 ** (len(num1) - 1 - i)
#         n1 = n1 * multiply_n1_10  # Scale n1 by its place value
#         print(f"n1 multiplied by 10^{len(num1) - 1 - i}: {n1}")
#         j = len(num2) - 1  # Reset j for each digit of num1
        
#         while j >= 0 or carry > 0:
        
#             n2 = int(num2[j]) if j >= 0 else 0
#             multiply_n2_10 = 10 ** (len(num2) - 1 - j)
#             n2 = n2 * multiply_n2_10
#             print(f"n2 multiplied by 10^{len(num1) - 1 - j}: {n2}")
            

#             print(f"n1: {n1}, n2: {n2}, carry: {carry}")
        
#             product = n1 * n2 + carry
#             print(f"Product: {product}")
#             carry = product // (max(multiply_n2_10, multiply_n1_10) * 10)
#             print(f"Carry: {carry}")
#             curr = product % (max(multiply_n2_10, multiply_n1_10) * 10)
#             print(f"Current digit: {curr}")
        
#             res.append(str(curr))
#             print(f"Result so far: {''.join(res[::-1])}")
#             j -= 1
        
#         i -= 1
        
#         num3 = int(''.join(res[::-1]))  # Reverse the result list and

#     return str(num3)

def multiply_large_numbers_v2(num1, num2):
    print()
    print(f"Multiplying {num1} and {num2}")
    num3 = 0
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    res = []
    numbers_to_add = []
    while i >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        print(f"Processing digit {n1} from num1 at index {i}")
        multiply_n1_10 = 10 ** (len(num1) - 1 - i)
        n1 = n1 * multiply_n1_10  # Scale n1 by its place value
        print(f"n1 multiplied by 10^{len(num1) - 1 - i}: {n1}")
        j = len(num2) - 1  # Reset j for each digit of num1
        
        while j >= 0 or carry > 0:
        
            n2 = int(num2[j]) if j >= 0 else 0
            multiply_n2_10 = 10 ** (len(num2) - 1 - j)
            n2 = n2 * multiply_n2_10
            print(f"n2 multiplied by 10^{len(num1) - 1 - j}: {n2}")
            

            print(f"n1: {n1}, n2: {n2}, carry: {carry}")
        
            product = n1 * n2
            numbers_to_add.append(product)
            j -= 1
        
        i -= 1
        
        #num3 = int(''.join(res[::-1]))  # Reverse the result list and
    
    for number in numbers_to_add:
        print(f"Adding {number} to num3")
        num3 += number

    return str(num3)

def multiply_large_numbers_submitted_first(num1, num2):
    num3 = 0
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    place = 0
    numbers_to_add = []
    while i >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        multiply_n1_10 = 10 ** (len(num1) - 1 - i)
        n1 = n1 * multiply_n1_10  # Scale n1 by its place value
        j = len(num2) - 1  # Reset j for each digit of num1
        
        while j >= 0 or carry > 0:
            n2 = int(num2[j]) if j >= 0 else 0
            multiply_n2_10 = 10 ** (len(num2) - 1 - j)
            n2 = n2 * multiply_n2_10
            product = n1 * n2
            numbers_to_add.append(product)
            j -= 1
        
        i -= 1
    
    for number in numbers_to_add:
        num3 += number

    return str(num3)

'''
Great question! Handling carry and digit placement is the trickiest part of manual multiplication.

    Instead of using powers of 10, try storing each digit of the result in a list, where the index represents its place value.
    When you multiply two digits, add the result to the correct index in this list, and handle the carry by updating the next index.

What do you think would happen if you always added the carry to the next position in your result list?'''

'''
Thanks for sharing your code! You’re still using powers of 10 and summing up large integers, which doesn’t quite follow the manual, digit-by-digit approach.

Try this instead:

    Create a result list of zeros with length len(num1) + len(num2).
    For each digit in num1 (from right to left), multiply it by each digit in num2 (also right to left).
    Add the product to the correct index in your result list.
    Handle carry by moving any value ≥10 to the next left index.

Can you try setting up that result list and see how you’d fill it in for each digit multiplication?'''

def multiply_large_numbers(num1, num2):
    num3 = 0
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    
    res = [0] * (len(num1) + len(num2))  # Result list initialized with zeros
    print(f"Initial numbers to multiply: {num1} and {num2}")
    print(f"zeroes in res: {res}")

    while i >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        j = len(num2) - 1  # Reset j for each digit of num1
        n2 = int(num2[j]) if j >= 0 else 0
        while j >= 0 or carry > 0:
            n2 = int(num2[j]) if j >= 0 else 0
            print(f"i: {i}, j: {j}\nn1: {n1}, n2: {n2}")
            product = n1 * n2 
            print(f"Product of {n1} and {n2} with carry {carry}: {product}")
            carry = product // 10  # Calculate carry for the next position
            print(f"Carry for next position: {carry}")
            curr = product % 10  # Current digit to add to result
            print(f"Current digit to add to result: {curr}")
            res[i + j + 1] += curr
            res[i + j] += carry
            
            if res[i + j + 1] >= 10:
                print(f"Handling carry for res[{i + j + 1}]: {res[i + j + 1]}")
                new_carry = res[i + j + 1] // 10
                res[i + j + 1] %= 10
                res[i + j] += new_carry
            print(f"Result after multiplying {n1} and {n2}: {res}")
            # if (len(num1) - i + len(num2) - j - 1) < len(res):
            #     carry = res[len(num1) - i + len(num2) - j - 1]
            # print(f"i: {i}, j: {j}, n1: {n1}, n2: {n2}, carry: {carry}")
            # print(f"Multiplying {n1} from num1 and {n2} from num2")

            # product = n1 * n2 + carry
            # print(f"Product: {product} due to n1: {n1} times n2: {n2} plus carry: {carry}\n{n1} * {n2} + {carry} = {product}")
            # carry = product // 10
            # print(f"Carry: {carry}")
            # curr = product % 10
            # print(f"Current digit to add to result: {curr}")
            # print(f"Adding {curr} to result at position {len(num1) - 1 - i + len(num2) - 1 - j}")
            # res[len(num1) - 1 - i + len(num2) - 1 - j] += curr
            # print(f"Result so far: {res}")
            # print(f"Adding carry {carry} to the next position: {len(num1) - 1 - i + len(num2) - 1 - j + 1}")
            # res[len(num1) - 1 - i + len(num2) - 1 - j + 1] = carry  # Add carry to the next position
            # print(f"Result so far: {res}")
            # #carry = res[len(num1) - 1 - i + len(num2) - 1 - j + 1]
            j -= 1
        
        i -= 1
        print(f"Result at i: {i} and j: {j} after multiplying {n1} and {num2}: {res}")
        # if res[i + j] >= 10:
        #         print(f"Need to handle carry for res[{i + j}]: {res[i + j]}")
        #         new_carry = res[i + j] // 10
        #         new_mod = res[i + j] % 10
        #         res[i + j] = new_mod
        #         res[i + j - 1] += new_carry
        print(f"After processing digit {n1} from num1: {num1} and {n2} from num2 {num2} , res: {res}")
    
    num3 = str(int("".join(map(str,res))))  # Join the result list into a string and remove leading zeros

    return num3
print(multiply_large_numbers('9', '9'))  # Example usage

def multiply_large_numbers_submitted(num1, num2):

    num3 = 0
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    
    res = [0] * (len(num1) + len(num2))  # Result list initialized with zeros

    while i >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        j = len(num2) - 1  # Reset j for each digit of num1
        
        while j >= 0 or carry > 0:
            n2 = int(num2[j]) if j >= 0 else 0
            product = n1 * n2 
            carry = product // 10  # Calculate carry for the next position
            curr = product % 10  # Current digit to add to result
            res[i + j + 1] += curr
            res[i + j] += carry
            
            if res[i + j + 1] >= 10:
                new_carry = res[i + j + 1] // 10
                res[i + j + 1] %= 10
                res[i + j] += new_carry
            
            j -= 1
        i -= 1
    num3 = str(int("".join(map(str,res))))  # Join the result list into a string and remove leading zeros

    return num3