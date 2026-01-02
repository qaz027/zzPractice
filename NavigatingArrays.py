''' Lesson
Navigating Arrays and Overcoming Obstacles in Python
Introduction

Welcome! In today's lesson, we're tackling a thrilling task that combines basic operations with numbers and array manipulation. 
We will implement a "Move Until Obstacle" game using a linear integer array. 
Picture yourself as a game developer and get ready to dive into the fun world of creatively solving problems!
Task Statement

In this "Move Until Obstacle" game, the player begins at the start of a linear array of integers. 
The number at each position indicates the number of steps a player can move rightward, while an obstacle number is one upon which you can't land. 
The aim is to move as far right as possible until an obstacle stops you or you reach the array's end.

Your function, solution(numbers, obstacle), needs to tally and return the number of moves needed to reach the array's end without encountering an obstacle. 
If the player encounters an obstacle, then the function should return the index at which the obstacle lies.

For example, if the function is given the input: numbers = [2, 3, 3, 4, 2, 4] and obstacle = 4, it should return 5. 
This is because the player starts on the 0th index, takes 2 steps as indicated by the number at the 0th index (landing on the 2nd index), and 
then takes 3 more steps as indicated by the number at the 2nd index to land on the 5th index, which is the obstacle 4.

If the function is given the input: numbers = [4, 1, 2, 2, 4, 2, 2] and obstacle = 2, the output should be 2. 
The player starts on the 0th index, takes 4 steps, lands on the 4th index, then takes 4 more steps, which brings the player outside the array, so in total the player makes 2 moves.
Solution Building: Step 1

Our first step is to ensure that we have variables to track the player, i.e., their current position and the moves they've taken so far. 
We'll call them position and moves, with both being initialized to 0:
```python
def solution(numbers, obstacle):
    position = 0
    moves = 0
    
Solution Building: Step 2 - Main Loop

Next, we'll use a while loop to iterate over the array. It continues as long as position is less than the size of the numbers array:
```python
    while position < len(numbers):
        
Solution Building: Step 3 - Obstacle Check

Within each iteration, we need to check if the player has met an obstacle. If so, return the position at which this obstacle resides:
```python
        if numbers[position] == obstacle:
            return position
            
Solution Building: Step 4 - Move Player and Increment Steps

If the current number is not an obstacle, the player proceeds. The number of steps taken is the value at the current position. We add this to position and increment moves:
```python
        moves += 1
        position += numbers[position]
        
Final Solution: Outside the Loop

Once the loop ends, either the player has reached the array's end or encountered an obstacle. 
If the player has navigated the entirety of the array without encountering an obstacle, we want the total moves to be returned:

    return moves
    

The complete solution looks like this:
```python

def solution(numbers, obstacle):
    position = 0
    moves = 0
    while position < len(numbers):
        if numbers[position] == obstacle:
            return position
        moves += 1
        position += numbers[position]
    return moves

Lesson Summary

Congratulations on successfully implementing the "Move Until Obstacle" game using Python! 
You've navigated task challenges by applying concepts of basic array manipulation and operations with numbers. 
Celebrate your achievements, but don't stop there! Up next, we have practice sessions filled with similar exercises to reinforce your understanding and skill. So, gear up and let's keep going! 
'''

def lesson_solution(numbers, obstacle):
    position = 0
    moves = 0
    while position < len(numbers):
        if numbers[position] == obstacle:
            return position
        moves += 1
        position += numbers[position]
    return moves

''' Exercise 1

You are given an array of n integers, ranging from 1 to 100 inclusive. 
Each integer represents a player's progress on a linear gameboard, indicating how many steps they can move to the right. 
However, the course is fraught with challenges; there exist several obstacles, represented by negative integers.

Your task is to return a transformed array structuring the gameboard in a new way: if an integer can lead the player to an obstacle on its right (within the range of its value), 
replace the number with the index of the obstacle. If the number represents an obstacle (a negative integer), replace it with -1. 
If none of these conditions are met, retain the original integer.

Keep in mind, this task is an innovative take on our previous analysis lesson, implementing a "Move Until Obstacle" game. 
Remember, your array will have no more than 500 elements, and the elements in the array range from -100 to 100, inclusive. Good luck with your coding journey!

For instance, given an array [3, 2, -3, 1, 2], the output would be [2, 2, -1, 1, 2].

Here's how it works:

    Replace the first position with 2 because a player at the first position can move 3 steps but will hit the obstacle at the 2nd index.
    Replace the second position with 2 because a player at the second position can move 2 steps but will hit the obstacle at the 2nd index.
    Replace the negative number -3 at the third position with -1 because it represents an obstacle.
    Keep the number 1 at the fourth position as there are no obstacles in its range.
    Keep the number 2 at the fifth position as there are no further positions or obstacles to impact it.
'''

def move_until_obstacle(gameboard):
    result = []
    n = len(gameboard)
    position = 0
    encountered_obstacle = 0
    while position < n:
        moves = gameboard[position]
        move = 1
        print(f"Current position: {position}, Moves: {moves}, Gameboard: {gameboard}, Result: {result}")
        if moves < 0:
            encountered_obstacle = 1
            print(f"Encountered obstacle at position {position} with value {moves}")
            result.append(-1) # element is an obstacle so return -1
            position += 1
            encountered_obstacle = 0 # reset obstacle flag
            continue
        # if move encounters an obstacle return the index of the obstacle
        while move <= moves and position + move < n:
            if gameboard[position + move] < 0:
                #result.append(position + move)
                encountered_obstacle = position + move
                print(f"Obstacle found at position {position + move} with value {gameboard[position + move]}")
                break
            #elif encountered_obstacle == 0:
                #result.append(moves)
            move += 1
        
        if encountered_obstacle:
            result.append(encountered_obstacle)
            print(f"Appending obstacle index: {encountered_obstacle}")
            #encountered_obstacle = 0
        else:
            print(f"No obstacle encountered, keeping original value: {moves}")
            result.append(moves)
        encountered_obstacle = 0 # reset obstacle flag
        position += 1 # increment position to check next element
    return result

test = [3, 2, -3, 1, 2] # Output: [2, 2, -1, 1, 2]
test = [1, 2, 3, 2, -3, 5, 2, 7, -1, 4] # Output: [1, 2, 4, 4, -1, 8, 8, 8, -1, 4]
test3 = [3, 4, -1, 2, 5, -2, 1, 5, 6] # Output: [2, 2, -1, 5, 5, -1, 1, 5, 6]
print(move_until_obstacle(test3))  


''' Exercise 2

Your task is to design a 1-dimensional game where a player moves along a path determined by an array of integers.

The path is an array of integers, each ranging from -100 to 100, inclusive. The size of the array n, i.e., the total number of steps on the path, can range from 1 to 500, inclusive. 
Each integer a_i in the array signifies how many steps the player can move and in which initial direction:

    A positive integer allows the player to move that many steps to the right.
    A negative integer directs the player to move that many steps to the left.
    Zero signifies a blockade that prevents further movement.

The game proceeds along the following rules:

    The player starts at the first position of the array (0-indexed) and moves according to the value at the player's current position in the array.

    If the value in the current position is zero, then the game ends. If the player's current position leads them outside of the array's boundaries, 
    then their ability to move in the current direction ceases.

    If the latter happens, then the player reverses their direction and continues to move according to similar rules, but now the directions are inverted: 
    positive integers lead the player to the left, and negative integers point to the right.

    The game ends when the player encounters a blockade or the array boundaries for the second time and so can no longer move.

You are to implement a function titled evaluatePath(numbers). This function should take an array of integers as input, representing the path and its rules, 
and return a tuple (position, moves), where:

    position: This is the player's final position (0-indexed) when the game ends.
    moves: This is the total number of moves made by the player until the game ends.

It's guaranteed that the game will not lead to an infinite loop, i.e. the path to the next blockade or the array boundaries would not require the player to visit the 
same position more than once.

For instance, given an array [3, 4, 1, 1, -3, 1]. The output would be (4, 5). Here's how it works:

    The player starts at position 0, where the value is 3. They move 3 steps to the right and land on the 3rd position. Total moves till now: 1.
    At position 3, the value is 1. They move 1 step to the right, landing on the 4th position. Total moves till now: 2.
    At position 4, the value is -3. They move 3 steps to the left, landing back on position 1. Total moves meanwhile: 3.
    At position 1, the value is 4. They move 4 steps to the right, landing on position 5. Total moves thus far: 4.
    At position 5, the value is 1, which would lead them out of the array's right boundary. So, they reverse their direction.
    After reversing direction at position 5, they move 1 step to the left and land on position 4. Total moves till now: 5.
    Now, with the reversed direction, the player is at position 4 where the value is -3. In the reversed direction, -3 indicates 3 steps to the right. 
    But this would again lead to the right boundary of the array. Since they have already reversed direction once, they cannot move further in any direction and the game ends.

At the end of the game, the player is at position 4 having made a total of 5 moves, thereby, the function returns (4, 5).'''

def evaluatePath(numbers):
    position = 0
    moves = 0

    l_bound = 0
    r_bound = len(numbers) - 1
    direction = 1  # 1 for right, -1 for left
    reversals = 0
    new_position = position + direction * numbers[position]

    print(f"Current position: {position}, Array output: {numbers[position]}, Moves: {moves}, Direction: {'Right' if direction == 1 else 'Left'}, ")

    while reversals < 2:
        if new_position < l_bound or new_position > r_bound:
            # Reverse direction
            direction *= -1
            reversals += 1
            if reversals == 2:
                break

        new_position = position + direction * numbers[position]
        if new_position < l_bound or new_position > r_bound: # still cannot find a valid position
                break

        moves += new_position != position   # Increment moves only if the position changes
        if moves == 0:
            # If the player is at the starting position and can't move, break
            break
        position += direction * numbers[position]
        new_position = position + direction * numbers[position]
        print(f"Current position: {position}, Array output: {numbers[position]}, Moves: {moves}, Direction: {'Right' if direction == 1 else 'Left'}, ")

    return (position, moves)  # Placeholder return statement, to be implemented

test_array = [3, 4, 1, 1, -3, 1]  # Expected output: (4, 5)
print(evaluatePath(test_array))  # Output: (4, 5)

test_array2 = [0]
print(evaluatePath(test_array2))  # Output: (0, 0)

test_array3 = [2, 1, -3, 4]
print(evaluatePath(test_array3))  # Output: (2, 1)

test_array4 = [3, 4, 1, 1, -3, 1]
print(evaluatePath(test_array4))  # Output: (4, 5)

''' Exercise 3

You are the developer of a unique board game and you need to calculate how many moves a player has to make, assuming different starting positions.

The game is played on a linear board represented by an array of positive integers. The length of the board can range from 11 to 500500 inclusive. 
Each position on the board represents the number of steps a player can make from that position. The player can only move towards the end of the board. 
The board can contain obstacles on which the player cannot land, defined by a specific integer value. The game ends when the player exits the board or lands on an obstacle.

Your task is to implement the solution(board, obstacle) function, which returns an array moves. 
For every i in moves, the algorithm should calculate the number of moves required for a player to exit the board, while starting from the i-th position, 
without landing on an obstacle. If the player encounters an obstacle, moves[i] should be set to -1.

The value of obstacle as well as each value in the board array ranges from 11 to 1010 inclusive.

For example, solution([5, 3, 2, 6, 2, 1, 7], 3) should return [3, -1, 3, 1, 2, 2, 1]. The moves array is calculated as follows:

    moves[0] should be 3 because:
        The player starts on board[0] = 5
        The player then moves 5 places on to board[5] = 1
        Then the player moves 1 place to board[6] = 7
        And, finally, the player moves to exit the board, making it a total of 3 moves

    moves[1] should be -1 because:
        The player starts on the board[1] = 3 which is equal to obstacle

    And so on...
'''

def moves(board, obstacle):
    outcomes = []
    n = len(board)

    for i in range(n):
        position = i
        move_count = 0
        while position < n:
            if board[position] == obstacle:
                outcomes.append(-1)
                break
            move_count += 1
            position += board[position]
            if position >= n:
                outcomes.append(move_count)
                break
    
    return outcomes