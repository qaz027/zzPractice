def solution(numbers):
    # TODO: implement this function
    result = []
    n = len(numbers)
    for i in range(n):
        geo_mean = round((numbers[i]*numbers[n-i-1])**0.5,2)
        result.append((numbers[i], geo_mean))
    print(result)

solution([1, 2, 3, 4, 5])
# Expected output: [(1, 2.24), (2, 2.83), (3, 3.46), (4, 4.47), (5, 5.0)]

isthisright = solution([1,2,3,4,5])==[(1, 2.24), (2, 2.83), (3, 3.0), (4, 2.83), (5, 2.24)]
print(isthisright)

results = []
results_sums = []
numbers = [1, 2, 3, 4, 5]
n = len(numbers)
for i in range(n):
    if i <= n/2:
    
        geo_mean = round((numbers[i]*numbers[n-i-1])**0.5,2)
        print(f"Geo mean of {numbers[i]} and {numbers[n-i-1]} is {geo_mean}")
        results.append((numbers[i], geo_mean))

print(results)

# Expected output:
#print(n, n/2)
numbers = [0,0,0,0]
n = len(numbers)
results_sums = []
half = n/2 if n%2==0 else (n//2 + 1)
for i in range(n):
    if i < half:
    
        #geo_mean = round((numbers[i]*numbers[n-i-1])**0.5,2)
        sum_pairs = numbers[i] + numbers[n-i-1]
        print(f"Sum of {numbers[i]} and {numbers[n-i-1]} is {sum_pairs}")
        results_sums.append(sum_pairs)

print(results_sums)
