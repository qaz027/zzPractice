'''
You are provided with an array of n integers, where n ranges from 11 to 501501 and is always an odd number. The elements of the array span values from −10^6 to 10^6, inclusive. 
The goal is to return a new array constructed by traversing the initial array in a specific order, outlined as follows:

    Begin with the middle element of the array.
    For each subsequent pair of elements, alternate between taking two elements from the left and two elements from the right, relative to the middle.
    If fewer than two elements remain on either side, include all the remaining elements from that side.
    Continue this process until all elements of the array have been traversed.

For example, for array = [1, 2, 3, 4, 5, 6, 7], your function should return [4, 2, 3, 5, 6, 1, 7]. 
And for array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], your function should return [6, 4, 5, 7, 8, 2, 3, 9, 10, 1, 11].'''

def solution(numbers):
    n = len(numbers)
    mid = n // 2
    odd = 1 if (n/2) % 2 == 1 else 0
    pairs = []
    
    # not needed - sequences are always odd 
    # if n % 2 == 1:
        # middle of the numbers array has no opposite
    left = mid - 1
    right = mid + 1
    pairs = [numbers[mid]]
        
    # else:
    #     left = mid - 1
    #     right = mid
    #     pairs = []
        
    while left >= 0 and right < n:
        if mid > 1: 
            pairs.extend([numbers[left], numbers[left-1],numbers[right], numbers[right+1]])
            left -= 2
            right += 2
            mid -= 2
        else:
            pairs.extend([numbers[left],numbers[right]])
            mid -= 1
            left -= 1
            right += 1
    return pairs

print(solution([1,2,3,4,5,6,7]))