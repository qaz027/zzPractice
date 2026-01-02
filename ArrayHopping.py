''' Lesson
Array Hopping Adventure: Exploring Index-Based Traversals
Introduction

Welcome to a delightful lesson on array traversal! Today, we invite you to join an endearing bunny named Gloria on an intricate quest. 
Gloria has a soft spot for number games, especially when they involve hopping between arrays. 
Our goal, on this exciting journey, is to assist Gloria through her escapade and identify the maximum value she encounters along the way. Are you ready to embark on this adventure?
Task Statement

Gloria's quest unravels with two arrays, both brimming with non-negative integers. 
Starting at the first element of arrayA, she leaps to arrayB based on the index she discovers in arrayA. 
She then bounces back to arrayA according to the index she stumbles upon in arrayB. Gloria repeats these hops until she returns to where she started in arrayA. What an adventure!

Your challenge is to craft a Python function that aids Gloria on her trip. 
The function will take two lists of integers as inputs, representing arrayA and arrayB. 
The objective is to find the highest value from arrayB that Gloria jumps to during her voyage.

It is guaranteed that at some point Gloria returns at the starting position.

Example

If arrayA = [2, 4, 3, 1, 6] and arrayB = [4, 0, 3, 2, 0], the output should be 3.

In this scenario, Gloria starts from the first element of arrayA, which is 2. Then, she jumps to arrayB at index 2, where she discovers 3. 
She then bounces back to arrayA at index 3, where she arrives at 1. From there, she leaps back to arrayB at index 1, stumbling upon a 0. 
Finally, she bounces back to arrayA at index 0, a location where she started her adventure. Hence she stops here and during this journey, she came across the highest value 3 from arrayB.
Solution Building: Step 1 - Initialization

Before we make headway with our code, let's kickstart with the initialization of variables. Let indexA and indexB denote the last positions of Gloria in arrayA and arrayB respectively. We will also use max_value for tracking the highest value encountered in arrayB. Her quest starts from arrayA, so we also maintain a Boolean flag in_arrayA.

indexA = 0
indexB = None
in_arrayA = True
max_value = float('-inf')

Solution Building: Step 2 - Array Hopping

Our assistant for Gloria’s hopping challenge will be a while loop! This keeps iterating until Gloria returns to her starting position in arrayA.

If Gloria is in arrayA, we check if the value in arrayB where she is going to land is greater than max_value, and update max_value if it is. 
We also switch Gloria's position to the other array in each iteration.

while True:
    if in_arrayA:
        indexB = arrayA[indexA]
        if arrayB[indexB] > max_value:
            max_value = arrayB[indexB]
    else:
        indexA = arrayB[indexB]
        if indexA == 0:
            return max_value
    in_arrayA = not in_arrayA


Final Function

Collecting all the pieces together, here's our ultimate function:

def solution(arrayA, arrayB):
    indexA = 0
    indexB = None
    in_arrayA = True
    max_value = float('-inf')
    while True:
        if in_arrayA:
            indexB = arrayA[indexA]
            if arrayB[indexB] > max_value:
                max_value = arrayB[indexB]
        else:
            indexA = arrayB[indexB]
            if indexA == 0:
                return max_value
        in_arrayA = not in_arrayA


Lesson Summary

Heartiest congratulations on guiding Gloria through her array hopping adventure. Not only have you heightened Gloria's joy, but you've also skillfully solved a complex task. 
You've deftly handled arrays, tracked indices, and made careful use of conditional statements.

This experience should empower you to take on more complex coding challenges. Keep practicing, keep exploring, and keep growing. Happy coding!'''

def lesson_arrayHopping(arrayA, arrayB):
    indexA = 0
    indexB = None
    in_arrayA = True
    max_value = float('-inf')
    while True:
        if in_arrayA:
            indexB = arrayA[indexA]
            if arrayB[indexB] > max_value:
                max_value = arrayB[indexB]
        else:
            indexA = arrayB[indexB]
            if indexA == 0:
                return max_value
        in_arrayA = not in_arrayA


''' Exercise 1

You're assisting in the creation of an algorithm for a novel game where a character hops between two arrays following certain rules. 
The game starts at the first index (1-based) of an array, arrayA.

The value at the character's current position in arrayA determines the index it jumps to on the second array, arrayB. 
Upon landing on arrayB, it does the same thing: the value at the current position specifies the index it jumps to in arrayA. 
This iteration continues until the character lands on an index in arrayA that it has already visited, at which point the game concludes.

Your task is to develop a Python function simulating this gameplay. The function receives two equal-length arrays of integers, arrayA and arrayB, each containing n elements (1 ≤ n ≤ 100). 
It should return an array consisting of the 1-based indices on arrayB that the character visited before a position on arrayA was repeated.

Each element in the input arrays ranges from 1 to n, indicating the next 1-based index that the character will jump to in the other array. 
The function guarantees that each jump always results in a valid position within the same-length arrays, and a position in arrayA will inevitably be revisited.

Can you devise a function that proficiently simulates this gameplay?

Example

For arrayA = [1, 3, 2, 5, 4] and arrayB = [5, 4, 3, 2, 1] the output should be [1, 4, 3, 2, 5] since it first lands at the first position in arrayB (the resulting array is [1]), 
then goes to the fifth position in arrayA, then returns to the fourth position in arrayB (the resulting array becomes [1, 4]), etc.'''

def traversing_arrays(arrayA, arrayB):
    indexA = 0
    indexB = None
    visited_Binidces = []
    repeated_indexA = False
    in_arrayA = True

    while not repeated_indexA:
        if in_arrayA:
            indexB = arrayA[indexA] - 1 # Convert to 0-based index
            visited_Binidces.append(indexB + 1)
            print(f"Visiting index {indexB + 1} in arrayB")

        else:
            indexA = arrayB[indexB] - 1 # Convert to 0-based index
            if arrayA[indexA] in visited_Binidces:
                return visited_Binidces
        in_arrayA = not in_arrayA
    
print(traversing_arrays([1, 3, 2, 5, 4], [5, 4, 3, 2, 1]))  # Example usage

''' Exercise 2

Gloria the bunny finds herself once again amidst an array game. This time, however, the game has slightly intensified with a third array coming into play. 
Your task is to develop a Python function to maneuver Gloria through her quest, yielding the summation of the maximum values she encounters from arrayB and arrayC together.

Gloria's journey begins at the first element of arrayA. Gloria's movement pattern follows a fixed sequence that repeats: arrayA -> arrayB -> arrayA -> arrayC. 
In other words, Gloria always alternates between arrayA and either arrayB or arrayC, following this pattern:

    First hop: arrayA to arrayB
    Second hop: arrayB to arrayA
    Third hop: arrayA to arrayC
    Fourth hop: arrayC to arrayA

Then the pattern starts over, continuing until the journey ends.

The rule to decide Gloria's move is: She uses the current element's value in the array as an index for her next array. 
For example, if Gloria is at arrayA[1]=2, she would move to arrayB[2].

The pattern repeats itself until one of the following occurs:

    Gloria's path repeats by visiting a position in arrayB or arrayC that was already visited, indicating that she is stuck in a loop and cannot progress further, OR
    Gloria tries to access an index that exceeds the length of an array (for example, attempting to access arrayA[4] when arrayA only contains 4 items indexed from 0 to 3), 
    in which case Gloria's journey should also stop.

Your task is to calculate the sum of the maximum values that Gloria encounters in arrayB and arrayC during her journey.

Each input array consists of n items, where n ranges from 11 to 100100, inclusive. Every item in the arrays is a non-negative integer and falls within the range of 00 to 9999, inclusive.

EXAMPLE

Consider arrayA = [2, 1, 3, 0], arrayB = [1, 3, 2, 4], and arrayC = [4, 2, 5, 1]. Gloria's journey would look like:

    She begins at arrayA[0] = 2 which leads her to arrayB[2] = 2.
    She then goes back to arrayA[2] = 3, and then to arrayC[3] = 1.
    She returns to arrayA[1] = 1, then makes a hop to arrayB[1] = 3.
    She goes back to arrayA[3] = 0 and then proceeds to arrayC[0] = 4.
    Now Gloria would go to arrayA[4], however, since arrayA[4] doesn't exist because arrayA only contains 4 elements indexed from 0 to 3, Gloria's journey stops here.

During her journey, Gloria encounters the maximum value 3 in arrayB and 4 in arrayC. The function should return 7, the sum of these two maximum values.'''

def gloria_journey(arrayA, arrayB, arrayC):
    indexA = 0
    indexB = None
    indexC = None
    max_B = float('-inf')
    max_C = float('-inf')
    visited_B_indices = []
    visited_C_indices = []
    step = 0 # 0 for arrayA->arrayB, 1 for arrayB->arrayA, 2 for arrayA->arrayC, 3 for arrayC->arrayA

    while True:
        if step == 0: # arrayA to arrayB
            indexB = arrayA[indexA]
            if arrayB[indexB] > max_B:
                max_B = arrayB[indexB]
            if indexB in visited_B_indices:
                break
            visited_B_indices.append(indexB)
            step = 1

        elif step == 1: #arrayB to arayA
            indexA = arrayB[indexB]
            if indexA >= len(arrayA):
                break
            step = 2

        elif step == 2: # arrayA to arrayC
            indexC = arrayA[indexA]
            if arrayC[indexC] > max_C:
                max_C = arrayC[indexC]
            if indexC in visited_C_indices:
                break
            visited_C_indices.append(indexC)
            step = 3
        
        elif step == 3: # arrayC to arrayA
            indexA = arrayC[indexC]
            if indexA >= len(arrayA):
                break
            step = 0

        

    return max_B + max_C

arrayA = [2, 1, 3, 0]
arrayB = [1, 3, 2, 4]
arrayC = [4, 2, 5, 1]
arrayA = [2, 0, 1]
arrayB = [1, 3, 2]
arrayC = [2, 0, 1]

print(gloria_journey(arrayA, arrayB, arrayC))  # Example usage

''' Exercise 3

Alice loves to play a jumping game on two parallel roads, roadA and roadB, each filled with integers. 
The game begins with Alice choosing a starting point on roadA, and then moving according to the following rules:

    Alice chooses a starting point on roadA.
    Each element in both the roads dictate exactly where to jump on the other road. 
    If Alice is at the ii-th position of roadA, where roadA[ii] = xx, then Alice moves to the xx-th position of roadB. 
    Likewise, if Alice is at the ii-th position of roadB, where roadB[ii] = yy, then she moves to the yy-th position of roadA.
    Alice continues these jumps until she ends up at an already visited spot on either road in the current route, which signifies the end of this game. 
    It's important to note that if a spot was visited in a previous route but not in the current route, it is not considered as an already visited spot.
    The distance covered in each jump is defined as 1 unit, no matter where she jumps to on the other road.

Your task is to create a function that receives these two roads, roadA and roadB, as its parameters. 
The function should calculate and return an array of total distances Alice covers during her game for each possible starting point on roadA. 
More specifically, the result should be an array results, where results[i] denotes the total distance covered if Alice starts from roadA[i].

The two input lists, roadA and roadB, contain nn and mm number of elements respectively. The number of elements in each list can range from 1 to 100, inclusive. 
Each element in roadA can have a value ranging from 0 to m−1m−1, inclusive. Similarly, each element in roadB can have a value ranging from 0 to n−1n−1, inclusive. 
This ensures that any element in either of the lists will be a valid index in the other list.

Example

For instance, if Alice's roads are given as roadA = [1, 0, 2] and roadB = [2, 0, 1], the function should return [2, 4, 4] because:

If Alice starts from roadA[0], her first jump takes her to roadB[1]. The value at this index tells her to jump to roadA[0], but since that's where she started this route 
(and thus it's already visited), she stops. As a result, Alice covers a total distance of 2 units.

If Alice starts from roadA[1], she jumps to roadB[0] which then redirects her to roadA[2]. From roadA[2], she jumps to roadB[1] which then leads her to roadA[0]. 
From roadA[0], she jumps to roadB[1] again but realizes this is the spot she has already visited in this route. Thus, in this case she covers a total distance of 4 units.

If Alice starts from roadA[2], her first jump takes her to roadB[2] and then the rule at this position directs her to roadA[1]. 
She has not yet visited roadA[1] in this route, so she follows the instruction and jumps to roadB[0], which also directs her to roadA[2], 
which she has visited in this route already so she stops there. Therefore, she covers a total distance of 4 units before landing on an already visited spot in her current route.'''

def AliceJumpingGame(roadA, roadB):
    moves = []
    visited_A = []
    visited_B = []
    step = 0
    for start in range(len(roadA)):
        print(f"Starting at index {start} from roadA: {roadA}")
        visited_A.clear()
        visited_B.clear()
        visited_A.append(start)
        print(f"Updating visited_A: {visited_A}")
        indexA = start
        indexB = None
        num_moves = 1
        # run sequence of steps jumping between 
        while True:
            if step == 0: #jump from roadA to roadB
                print(f"Step: {step}, indexA: {indexA}, roadA[{indexA}]: {roadA[indexA]}")
                indexB = roadA[indexA]
                if indexB in visited_B:
                    print(f"Already visited indexA: {indexB}, in visitedB array {visited_B} stopping the game.")
                    #moves.append(num_moves)
                    break
                visited_B.append(indexB)
                num_moves += 1
                step = 1
                print(f"Jumping to roadB at index {indexB}, which corresponds to {roadB[indexB]} step updated to {step}, num_moves updated to: {num_moves}")
            elif step == 1: #jump from roadB to roadA
                # Ensure indexB is initialized before using it
                if indexB is None:
                    indexB = roadA[start]
                print(f"Step: {step}, indexB: {indexB}, roadB[{indexB}]: {roadB[indexB]}")
                indexA = roadB[indexB]
                print(f"Jumping to roadA at index {indexA} which corresponds to {roadA[indexA]}")
                if indexA in visited_A:
                    print(f"Already visited indexA: {indexA}, in visitedA array {visited_A} stopping the game.")
                    #moves.append(num_moves)
                    break
                visited_A.append(indexA)
                print(f"Updated visited_A: {visited_A}")
                print(f"Visited_A after jump: {visited_A}, continuing the game.")
                num_moves += 1
                print(f"Updated number of moves: {num_moves}, visited_A: {visited_A}")
                step = 0
                print(f"Step updated to {step}, continuing the game. Number of moves updated: {num_moves}")

        moves.append(num_moves)
        step = 0  # Reset step for the next starting point
        


    return moves

roadA = [2, 2, 2, 2]
roadB = [3, 2, 1, 0]
roadA, roadB = [1, 2, 3, 0], [2, 3, 0, 1]

print(AliceJumpingGame(roadA, roadB))  # Example usage should return []

