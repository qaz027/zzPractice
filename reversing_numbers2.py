def solution(n):
    reverse_num = 0
    while n > 0:
        print(f"The input number is {n}")
        digit = n % 10
        print(f"The digit is {digit}")
        reverse_num = reverse_num * 10 + digit
        print(f"Updating the reverse number is {reverse_num}")
        n = n // 10
        print(f"Updating n is now {n}")
    
    print(f"The reverse number is now {reverse_num}")
    return reverse_num

print(solution(1234))


def solution(n):
    digit = 0
    iteration = 0
    doubled = 0
    while n > 0:
        print(f"n = {n}")
        multiplier = 10 ** iteration
        print(f"multiplier = {multiplier}")
        digit = (n % 10) * 11
        print(f"digit is = {digit}")
        doubled += (digit * multiplier)
        print(f"updating the number to return: {doubled}")
        n = n // 10
        print(f"updating for the next iteration")
        iteration += 2
    
    return doubled

print(solution(1234))

inputString = 'aa'
result_string = ''
n = len(inputString)
half = n // 2 + n % 2
iterator1 = n-1
iterator2 = 0 
print(f"n: {n}")
print(f'half: {half}')
    
for i in range(n-1,half-1 - n%2, -1):
    print(inputString[i])

for i in range(0,half-n%2):
    print(inputString[i])
    
while iterator1 >= half:
    result_string += inputString[iterator1]
    iterator1 -= 1
    
while iterator2 < half:
    result_string += inputString[iterator2]
    iterator2 += 1
    
print(result_string)