'''
You are given an array of n integers, where n can range from 1 to 500, inclusive. 
Your task is to create a new array in which each element is a tuple, determined by pairing elements from the middle to both ends of the original array.

If the original array has an odd length, pair the middle element with 0. If the original array has an even length, start pairing from the two middle elements. 
Continue the pairing by alternating elements from the left and the right until all elements have been paired.

After creating the paired elements, return the new array of tuples. Ultimately, your result should be an array of tuples, each of size two. 
Each element within a tuple, as well as within the array, can range from -1000 to 1000, inclusive.

For example, if the input is numbers = [1, 2, 3, 4, 5], the output should be [(3, 0), (2, 4), (1, 5)]. 
Similarly, if the input is numbers = [1, 2, 3, 4], the output should be [(2, 3), (1, 4)].
'''

def solution(numbers):
    n = len(numbers)
    mid = n // 2
    pairs = []
    
    if n % 2 == 1:
        # middle of the numbers array has no opposite
        left = mid - 1
        right = mid + 1
        pairs = [(numbers[mid],0)]
        
    else:
        left = mid - 1
        right = mid
        pairs = []
        
    while left >= 0 and right < n:
        pairs.append((numbers[left],numbers[right]))
        left -= 1
        right += 1
    return pairs

print(solution([1,2,3,4,5]))
