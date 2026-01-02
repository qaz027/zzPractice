''' Lesson 

Task Statement

Consider an array which symbolizes a dense forest; each index is either 1, indicating a tree, or 0, signifying a clear position. 
Starting from a fixed initial index and given a specific direction, your objective is to ascertain the smallest possible jump size that enables traversal from the initial position
to one of the ends of the array without hitting a tree. Each move you make will be exactly the determined jump size in the given direction.

Keep these pointers in mind:

    The array of binary integers (0 and 1) depicts the forest.
    The journey will always commence from a 0 index.
    The direction is an integer. 1 implies jumping toward larger indices, while -1 denotes jumping toward smaller ones.
    In situations where there is no jump size that can avoid all trees, return -1 to indicate the impossibility of traversal under these conditions.

The ultimate objective? Identify the minimal jump size that ensures a smooth navigation through the entire forest without hitting a single tree.

Example

For the input values forest = [0, 1, 0, 0, 0, 0, 1, 1], start = 0, and direction = 1, the output should be 4.

    If you take the jump size equal to 1, you immediately step on a tree.
    If you choose 2, you step on a tree after three jumps at forest[6].
    If you choose 3, you again step on a tree at forest[6].
    For the jump size equal to 4, you first jump to the 4th position which is a valid position, then jump outside of the array, thereby traversing the forest without hitting a tree.

Step 1: Start the Function

The first step involves initializing your function which takes as input the forest array, the start position, and the direction. We begin with a jump size of 1:

def calculate_jump(forest, start, direction):
   
    jump = 1

    # Other steps will be added here...


Step 2 - Implement the Jumping Mechanism

Now, we'll explore each potential jump size beginning from 1. At each jump size, implement a while loop to execute jumps of that designated size in the identified direction:

def calculate_jump(forest, start, direction):

    jump = 1

    while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
        pos = start
        while 0 <= pos < len(forest):
            
            # Subsequent steps follow...
            
        jump += 1

The condition on line 5 ensures the jumps stay within the boundary of the forest array. The expression (direction * jump) + start calculates the position index after executing a jump. 
When direction is 1, you are jumping towards larger indices, and when it's -1, you are jumping towards smaller indices.

The condition checks that this new position remains within the bounds of the forest (array). >=0 ensures you don't jump too far to the left to negative indices, and < len(forest) 
checks that you don't jump beyond the array's length on the right.


Step 3 - Check for Trees

Within the nested loop, inspect whether the current position has a tree. If it does, break the loop and examine the next jump size. If it doesn't, carry on jumping:

def calculate_jump(forest, start, direction):

    jump = 1

    while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
        pos = start
        while 0 <= pos < len(forest):
            if forest[pos] == 1:
                break
            pos += jump * direction
        else:
            return jump

        jump += 1
    return -1

Here, the function iterates over positive integers as potential jump sizes, starting from 1. For each size, it starts from the initial position and carries out jumps of that magnitude. 
If a tree is encountered, it halts, adds 1 to the jump size and tests again. If it doesn't encounter a tree and successfully jumps one end of the forest, it promptly returns the jump size. 
If no viable jump size is found after checking numbers up to the length of the forest, it returns -1.

Lesson Summary

Congratulations! You've mapped out a path to traverse through the forest and have created a function that identifies the its minimal safe jump size. 
This exercise has helped you sharpen your problem-solving skills, and become adept at Python, particularly array manipulation and control structures. 
Continue practicing and exploring different challenges to solidify these skills! 
We look forward to seeing you take on next challenge!
'''

def calculate_jump(forest, start, direction):

    jump = 1

    while (direction * jump) + start >= 0 and (direction * jump) + start < len(forest):
        pos = start
        while 0 <= pos < len(forest):
            if forest[pos] == 1:
                break
            pos += jump * direction
        else:
            return jump

        jump += 1
    return -1


''' Exercise 1

You are given an array of n integer values, with n ranging from 1 to 500, inclusive. The array represents a path through a virtual dungeon, with certain positions marked as traps.

Each element in the array ranges from −10^10 to 10^10, inclusive, and represents the trap power. A value of 0 signifies a safe position, 
whereas positive integers indicate trap power — the higher the value, the harder it is to avoid and, hence, the more dangerous it is. 
Negative integers are traps that are easier to avoid, with negative values implying that the trap could potentially aid you rather than hinder.

Your task is to move from the start position to the end position. For each step, you can move by x elements in the right direction only, where x ranges from 1 to n. 
Each time you step on a trap, you lose health points equal to the trap's power. You originally have h health points, where h is a positive integer ranging from 1 to 10^100.

Find the x that you must choose such that you lose the least amount of health points upon reaching the end of the array. 
Also, determine if there is no possible x that allows you to reach the end of the array with any remaining health points. 
In the latter case, return -1 to indicate that it's impossible to traverse the dungeon without succumbing to a fatal trap. 
If at any point your health points reach 0 or less, you are considered out of the game.

Example

Input:

    Array of trap powers: [0, 5, -2, 8, 3, 0, 10, 4, -1, 7]
    Initial health: 20

Process: Let's analyze different step sizes (x) to find which one minimizes health loss:

Step size x = 1:

    Path: 0 → 5 → -2 → 8 → 3 → 0 → 10 → 4 → -1 → 7
    Health loss: 0 + 5 + (-2) + 8 + 3 + 0 + 10 + 4 + (-1) + 7 = 34
    Since 34 > 20, with step size 1, you would lose all health before reaching the end.

Step size x = 2:

    Path: 0 → -2 → 3 → 10 → -1
    Health loss: 0 + (-2) + 3 + 10 + (-1) = 10
    Remaining health: 20 - 10 = 10

Step size x = 3:

    Path: 0 → 8 → 0 → 4 → 7
    Health loss: 0 + 8 + 0 + 4 + 7 = 19
    Remaining health: 20 - 19 = 1

Step size x = 4:

    Path: 0 → 3 → 4
    Health loss: 0 + 3 + 4 = 7
    Remaining health: 20 - 7 = 13

Step size x = 5:

    Path: 0 → 0 → 7
    Health loss: 0 + 0 + 7 = 7
    Remaining health: 20 - 7 = 13

Step size x = 6:

    Path: 0 → 10
    Health loss: 0 + 10 = 10
    Remaining health: 20 - 10 = 10

Step size x = 7:

    Path: 0 → 4
    Health loss: 0 + 4 = 4
    Remaining health: 20 - 4 = 16

Step size x = 8 (optimal):

    Path: 0 → -1
    Health loss: 0 + (-1) = -1 (actually gaining 1 health)
    Remaining health: 20 - (-1) = 21

Step size x = 9:

    Path: 0 → 7
    Health loss: 0 + 7 = 7
    Remaining health: 20 - 7 = 13

Step size x = 10:

    Cannot reach the end of the array with this step size, as it would overshoot the array.

Output:

    Optimal step size (x): 8
    Minimum health loss: -1 (you actually gain 1 health point)
    Remaining health: 21

Additional Example

If we changed the initial health to be only 3, and the trap values to [0, 5, 10, 8, 3, 20, 10, 4, 30, 7], 
then there would be no possible step size that allows you to reach the end with remaining health, so the output would be -1.
'''

def paths_to_take(dungeon, health):

    optimal_path = False
    path_outcome = []
    step_sizes = len(dungeon)
    path_health = health
    optimal_step = 0


    for step in range(1,step_sizes+1):
        print(f"Step size is {step}")
        for n in range(0,len(dungeon),step):
            print(f"step {n+1}: Dungeon[{n}]: {dungeon[n]}")
            #progress through dungeon taking each step
            path_health -= dungeon[n]
            print(f"Health update: {path_health}")
        path_outcome.append(path_health)
        print(f"Update to path outcome: {path_outcome}")
        if path_health >= max(path_outcome):
            optimal_step = step
        path_health = health
        
    optimal_path = max(path_outcome)
    if optimal_path < 0:
        optimal_path = False
        

    if optimal_path == False:
        return -1
    else:
        return optimal_path, path_outcome.index(optimal_path), optimal_step

test = [0, 5, -2, 8, 3, 0, 10, 4, -1, 7]
test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
initial_health = 10
#print(paths_to_take(test, initial_health))

''' Exercise 2

Assume you have a community garden composed of n different types of flowers, with n ranging from 1 to 100. Each type is represented by a distinct number (1, 2, 3, ..., n). 
The garden is depicted as a 1D array, wherein each element indicates the type of flower planted in that specific location.

Your task involves visiting each type of flower at least once, traversing the garden in a specific direction (either from left to right with smaller to larger indices, 
or from right to left). You can take exactly k number of steps in the chosen direction, visiting a new location.

Write a Python function, largest_step(garden, start, direction), that accepts as input the garden as an array, your starting position, and the direction in which you want to travel. 
This function is expected to compute and return the largest-sized step step that you can take so that you can visit each type of flower existing in the garden at least once.

If no such value of step enables you to visit all types of flowers at least once, the function should return -1. The direction is given as an integer — 1 indicates moving towards 
larger indices (right), while -1 suggests moving towards smaller ones (left).
'''

def largest_step(garden, start, direction):
    largest_step = -1

    unique_flowers = {}

    # create a dict of unique flowers in the garden array
    for flower in garden:
        if flower not in unique_flowers:
            unique_flowers[flower] = 1

    print(f"the unique flowers are {unique_flowers}")
    print(f"the length of the garden path is {len(garden)}")
    
    if direction == 1:
        print(f"we are traversing from small to large")
        # traverse the garden from small to large indices
        for step_size in range(1,len(garden)+1-start):
            # reset unique flowers:
            for key in unique_flowers.keys():
                unique_flowers[key] = 1
            print(f"the unique flowers are {unique_flowers}")
            print(f"step size is {step_size}")
            for i in garden[start::step_size]:
                unique_flowers[i] +=1
                print(f"the unique flowers are {unique_flowers}")
                if all(values > 1 for values in unique_flowers.values()):
                    print(f"updating step size to {step_size}")
                    largest_step = step_size



    else: # traverse the garden from large to small indices
        print(f"we are traversing from large to small")
        for step_size in range(start, 0, -1):
            for key in unique_flowers.keys():
                unique_flowers[key] = 1
            print(f"step size is {step_size}")
            for i in garden[start::-step_size]:
                unique_flowers[i] +=1
                print(f"the unique flowers are {unique_flowers}")
                if all(values > 1 for values in unique_flowers.values()):
                    print(f"updating step size to {step_size}")
                    largest_step = step_size
                    return largest_step

    return largest_step

#print(largest_step([1, 1, 1, 1, 1, 1, 1], 6, -1))
#print(largest_step([1, 2, 3, 4, 5, 9, 2, 1, 3, 8, 2, 7, 1, 6], 13, -1))

''' Exercise 3
Prepare to challenge your array manipulation skills! Consider two arrays, array1 and array2, each consisting of n non-negative integers. The values of n range from 1 to 500, inclusive. 
Each integer in the arrays is at most 10^3.

Your task is to discover a rotation of array1 that minimizes the Manhattan distance with array2. The Manhattan distance between two arrays, a and b, of size n, is defined by:
D(a,b)=∑i=1n∣ai−bi∣

where aiai​ and bibi​ denote the ii-th elements of arrays a and b, respectively, and nn represents the size of the arrays.

A rotation of an array refers to taking one or more elements from the end and moving these elements to the beginning, maintaining their original order in the process.

You need to return the smallest possible Manhattan distance obtained through this operation.

Let's say that you find multiple rotations of array1 that yield the same smallest Manhattan distance with array2. 
In this case, you should return the rotated array that, when converted into an integer number by concatenating all of its digits (from left to right), would be the smallest.

Consider the array as periodic; that is, after the last element, the first one follows.

Keep in mind that the size of the two arrays is always the same, and the arrays are not necessarily sorted at the beginning.

If array1 is exactly the same as array2 from the beginning, output the original array1 and the Manhattan distance 00.

Remember, the ultimate goal is to minimize the Manhattan distance between array1 and array2 through the least alterations possible to array1. Let's see how small you can get!
'''

def manhattan_distance(array1, array2):

    distance = 0
    min_distance_array_cat = ''
    array1_cat = ''

    print()
    

    def calc_manh_distance(array1, array2):
        print(f"calculating Manhattan Distance for {array1} and {array2}")
        distance = 0
        for i in range(len(array1)):
            if array1[i] > array2[i]:
                distance += array1[i] - array2[i]
            else:
                distance += array2[i] - array1[i]
        print(f"Distance is {distance}")
        return distance
            

    min_distance_array = array1[:]
    print(f"Initializing min distance array")
    min_distance = calc_manh_distance(array1, array2)

    for i in min_distance_array:
        min_distance_array_cat += str(i)
    min_distance_array_cat_num = int(min_distance_array_cat)
    

    
    # use array1.insert(0,array1.pop()) to move the last elements to the front

    for i in range(len(array1)-1):

        array1.insert(0, array1.pop())
        print(f"New array1 is: {array1}")

        distance = (calc_manh_distance(array1, array2))

        if distance > min_distance:
            continue
        
        if distance < min_distance:
            print(f"distance is less than current min distance. Updating manhanttan distance...")
            min_distance = distance
            print(f"Updated min_distance to {min_distance}")
            min_distance_array = array1[:]
            print(f"Updated min distance array to {min_distance_array}")
            min_distance_array_cat = ''
            for i in min_distance_array:
                min_distance_array_cat += str(i)
                min_distance_array_cat_num = int(min_distance_array_cat)
        elif distance == min_distance:
            print(f"new distance is equal to current min distance. Must check concatenated array strings to see which is smaller...")
            for i in array1:
                array1_cat += str(i)                
            array1_cat_num = int(array1_cat)
            
            print(f"Array1 concatenated string is {array1_cat_num} and comparing against {min_distance_array_cat_num}")
            if array1_cat_num < min_distance_array_cat_num:
                print(f"Array1 string: {array1_cat_num} is less than min_distance string: {min_distance_array_cat_num}")
                min_distance = distance
                print(f"Distance: {distance}")
                min_distance_array = array1[:]
                print(f"Updating min distance array: {min_distance_array}")
                min_distance_array_cat = array1_cat
                min_distance_array_cat_num = array1_cat_num

        print(f"Summary of iteration: ")
        print(f"i: {i}")
        print(f"Array 1: {array1}")
        print(f"Min Distance: {min_distance}")
        print(f"Min Distance array: {min_distance_array}")
        print('-'*150)
        distance = 0

    return (min_distance_array, min_distance)
    
array1, array2 = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]
array1, array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(manhattan_distance(array1,array2))

def manhattan_submitted(array1, array2):
    distance = 0
    min_distance_array = []
    min_distance_array_cat = ''
    array1_cat = ''
    
    def calc_manh_distance(array1, array2):
        distance = 0
        for i in range(len(array1)):
            if array1[i] > array2[i]:
                distance += array1[i] - array2[i]
            else:
                distance += array2[i] - array1[i]
    
        return distance
            
    min_distance_array = array1[:]
    min_distance = calc_manh_distance(array1, array2)

    for i in min_distance_array:
        min_distance_array_cat += str(i)
    min_distance_array_cat_num = int(min_distance_array_cat)

    for i in range(len(array1) - 1):

        array1.insert(0, array1.pop())
        distance = (calc_manh_distance(array1, array2))
        
        for i in array1:
            array1_cat += str(i)
        array1_cat_num = int(array1_cat)

        if distance > min_distance:
            continue
        
        if distance < min_distance:
            min_distance = distance
            min_distance_array = array1[:]
            min_distance_array_cat = array1_cat
            min_distance_array_cat_num = array1_cat_num
        elif distance == min_distance and array1_cat_num < min_distance_array_cat_num:
            min_distance = distance
            min_distance_array = array1[:]
            min_distance_array_cat = array1_cat
            min_distance_array_cat_num = array1_cat_num
        
        array1_cat = ''

    return (min_distance_array, min_distance)