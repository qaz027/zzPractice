
numbers = [12, 21, 34, 43, 56, 65]

for n in numbers:
    print(n, end=": ")
    temp = str(n)
    rev = ""
    for i in range(len(temp) - 1, -1, -1):
        rev += temp[i]
        #print(temp[i], end="")
    rev = int(rev)  # Convert the reversed string back to an integer
    print(rev)  # New line after each number's reverse output