''' Lesson 
Nested Loop Pair Discovery: Comparing Elements Across Two Arrays
Introduction

Hello and welcome to today's programming practice session! Are you prepared to delve into an exciting task involving nested loops and arrays? 
Our focus today will be on mastering the use of nested loops to search two arrays. You're about to embark on a fascinating journey of hands-on learning. Let's get started!
Task Statement

Imagine you've received two lists of integers. Should you choose to accept this mission, you'll need to write a function that locates and returns pairs of integers. 
The first element of the pair will come from the first list, with the second coming from the second list. Important to note is that the first element must be less than the second.

The order of pairs in your result should follow the order in which they appear in the input lists. 
For instance, given the lists [1, 3, 7] and [2, 8, 9], the function should return [(1, 2), (1, 8), (1, 9), (3, 8), (3, 9), (7, 8), (7, 9)]. 
It's a challenge if no pairs exist, or if any input list is empty. Let's dissect this task to unravel the solution together!

Solution Building: Step 1

Before we dive into writing code, let's break down the problem. It appears to be an ideal candidate for nested looping.

Begin by initializing an empty list called result, which will store our pairs.

Python

def solution(list1, list2):

    result = []


    It's always prudent to set up your function and data storage first!

Solution Building: Step 2

In this step, our focus shifts to the creation of nested loops. We'll need to iterate over both lists simultaneously. 
To do this efficiently, we'll use nested loops. One outer loop will pick an element from the first list, and an inner loop will skim through each element of the second list.

Python

def solution(list1, list2):

    result = []

    for i in list1:

        for j in list2:

            # We'll fill this in next

    return result

In this context, i represents each element in list1, and for each i, j represents each element in list2.
Solution Building: Step 3

Now that we have our loops established, let's introduce the logic inside. Here's where we make a crucial check: 
Is the element i from list1 lesser than the element j from list2? If it is, we append the pair (i, j) to our result list.



def solution(list1, list2):

    result = []

    for i in list1:

        for j in list2:

            if i < j:

                result.append((i, j))

    return result

During each iteration of our inner loop, we make this check and store the pairs that meet our condition.
Lesson Summary

Excellent job! You've successfully implemented a complex task using nested loops to search two arrays. 
You now know how to traverse and manipulate two lists effectively to achieve your desired objective. 
Keep practicing and continually challenge yourself with more tasks to consolidate your knowledge. 
In your subsequent practice sessions, you will encounter similar challenges that will further enhance your understanding of this concept. 
Remember, practice is the key to mastering any concept. Happy coding!
'''

''' Example 1

You are provided with two arrays of unique integers, with the lengths of arrays ranging from 1 to 100, inclusive. 
The task requires you to identify elements that appear in both arrays and return them in an array, maintaining the order from the first provided array.

Each array's element ranges from -100 to 100, inclusive.

In your function common_elements(listA, listB), listA and listB represent the two input arrays. 
The function should return an array that includes the common elements found in both listA and listB, while preserving the order of elements as they appear in listA.

For example, if listA = [7, 2, 3, 9, 1] and listB = [2, 3, 7, 6], the output should be [7, 2, 3].'''

def common_elements(listA, listB):
    result = []
    
    for a in listA:
        for b in listB:
            if a == b:
                result.append(a)
    
    return result

''' Example 2

You are given two lists: sourceArray and searchArray, consisting of n and m tuples respectively, where n is an integer such that 1 ≤ n ≤ 100 and m is an integer such that 1 ≤ m ≤ 500. 
Each tuple in both arrays contains two elements: an integer identifier and a string. The identifiers in both arrays range from 1 to 100, inclusive. 
The strings in sourceArray consist of alphanumeric characters with lengths ranging from 1 to 100, inclusive. The strings in searchArray have lengths ranging from 1 to 500, inclusive.

Your task is to implement a function stringSearch(sourceArray, searchArray) that takes these two arrays as input and returns an array that includes all tuples from 
sourceArray for which its string is a substring of at least one string in any tuple from searchArray and the identifier of the source tuple is less than or equal to the identifier of the search tuple.

The order in which the tuples appear in the result should reflect their original order in the sourceArray. If no matches are found, the function should return an empty array.

For example, if sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')] and searchArray = [(1, 'abcdef'), (5, 'uvwxy')], the function should return [(1, 'abc')] since 'abc' and 'def' are substrings 
found in 'abcdef', but 'def' is associated with 2 in sourceArray which is not less than or equal to 1 in searchArray. The string 'xyz' is not found in either 'abcdef' or 'uvwxy', so it is not included in the result.

This task requires mastery of skills in nested looping and array manipulation, especially in the context of searching for a string within other strings.'''

def stringSearch(sourceArray, searchArray):
    # TODO: implement
    pass
