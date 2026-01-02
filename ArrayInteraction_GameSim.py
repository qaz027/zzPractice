''' Lesson
Exploring Array Interactions through Simulation Games
Introduction

Welcome! Are you ready to embark on a captivating journey into the world of array manipulations? Today, we're going to explore a fascinating scenario involving a wonderful small town, its houses, and a fun balloon game. Without further ado, let's dive right in!
Task Statement

Picture a quaint, small town where every house is numbered sequentially from 1 to n. One day, a festive town event is held, and balloons are tied to each house. The festivities do not end there. At the conclusion of the event, a fun game is played: at each step of the game, each house sends half of its balloons to the neighboring house simultaneously (the neighbor on the right side, and for the last house, the neighbor is the first house). The game goes on until at some step there are no changes in the amount of balloons compared to the previous step.

The task is to create a Python function, solution(balloons), where balloons is a list representing the number of balloons at each house. The function should simulate this game and return the number of steps in the game.

For example, if balloons = [4, 1, 2], the output should be solution(balloons) = 3. After the first step, the list becomes [3, 3, 1]. This is because the first house sends 2 balloons and gets 1, the second house sends nothing but gets 2, and the third house sends 1 but receives nothing. Note that when the number of balloons x is odd, than the house sends (x - 1) / 2 balloons. After the second step, the list becomes [2, 3, 2] and never changes after that. So after the third step, the process finishes.
Solution Building: Step 1 - Understanding the Problem

Firstly, it's essential to note that we're dealing with a cyclical event. In other words, when iterating over our balloons array, we need to perceive the array as circular, meaning balloons[n - 1] should refer back to balloons[0]. This concept of cyclicity becomes crucial when we consider the last house passing balloons to the first.
Solution Building: Step 2 - Setting Up The Loop

Confident in our understanding of the problem, we move on to programming our solution. First, we need to set up a loop to iterate the rounds of the balloon sharing. This loop should continue as long as the list changes.

Python

def solution(balloons):

    steps = 0

    while True:

        steps += 1

        new_balloons = balloons.copy()  # Store updated balloon counts

        # TODO: Share the balloons

        if new_balloons == balloons:

            break

        balloons = new_balloons # Update balloons with new counts.

    return steps

Solution Building: Step 3 - Sharing Balloons

Our next step delves into the core game mechanics: sharing the balloons. Throughout each cycle, each house must share half of its balloons with the next house.

We must also ensure that the last house shares balloons with the first house at the end of each cycle — for this, we'll use the handy modulo % operator.

Here's the updated solution, complete with the mechanics of balloon sharing:

Python

def solution(balloons):

    n = len(balloons)

    steps = 0

    while True:

        steps += 1

        new_balloons = balloons.copy()

        for i in range(n):

            share = balloons[i] // 2  # Balloons to share

            new_balloons[i] -= share  # Decrease balloons of current house.

            new_balloons[(i + 1) % n] += share  # Increase balloons of next house.

        if new_balloons == balloons:

            break

        balloons = new_balloons

    return steps

Bravo! We've navigated through the maze of array manipulation and successfully simulated an intriguing game event.
Lesson Summary

Congratulations on mastering this crucial programming scenario! You've successfully navigated a task involving the simulation of real-world events using array manipulation.

What's next? Now is the time to put into practice everything we've learned today. Try designing different versions of this balloon sharing game. As always, happy coding!
'''

def lesson_solution(balloons):
    n = len(balloons)
    steps = 0
    while True:
        steps += 1
        new_balloons = balloons.copy()
        for i in range(n):
            share = balloons[i] // 2  # Balloons to share
            new_balloons[i] -= share  # Decrease balloons of current house.
            new_balloons[(i + 1) % n] += share  # Increase balloons of next house.
        if new_balloons == balloons:
            break
        balloons = new_balloons
    return steps

# I don't really understand new_balloons[(i+1) % n] += share

''' Exercise 1

You are given a string s containing only uppercase letters, with its length n ranging from 1 to 100, inclusive. Your task involves series of sequential comparisons resulting 
in the removal of certain characters, following this process:

    Form neighbouring pairs in the string sequentially (pair the first and second characters, the third and fourth, and so forth). If the string length is odd, keep the 
    last character unpaired.
    For each pair, compare the characters and remove the character that comes earlier in the lexicographical order. If they are the same, remove the first character in the pair.
    These two steps define a round of operation. Perform these rounds until the string becomes empty.
    If the string length after a round is 1, in the next round the last remaining character is removed and the process terminates.

Your task is to implement a Python function, solution(s), where s is the initial input string. The function should follow the described process and return a list of the removed 
letters in the order of their removal.

Each character of the string is an uppercase letter from A to Z, inclusive.

As an example, if s = "BCAAB", the output should be ['B', 'A', 'A', 'B', 'C'].

The rounds would occur as follows:

    After the first round, the pairs are (B,C), (A,A), (B) and the resulting string is CAB with 'B' and 'A' being removed. The removed characters list becomes ['B', 'A'].
    After the second round, the pairs are (C,A) and (B), and the resulting string is CB with 'A' being removed. The removed characters list becomes ['B', 'A', 'A'].
    After the third round, B is removed and the string becomes C. The removed characters list becomes ['B', 'A', 'A', 'B'].
    After the fourth round, there are no pairs, and thus 'C' is removed, and the resulting string is empty. The removed characters list becomes ['B', 'A', 'A', 'B', 'C'].

'''

def compare_pairs(s):

    eliminated = []
    
    while s != '':
        n = len(s)
        s_new = ''
        for i in range(0,n,2):
            print(f"i: {i}")
            if i+1 == n:
                pairs = [s[i]]
            else:
                pairs = [s[i], s[i+1]]
            print(f"pairs: {pairs}")

            if len(pairs) == 1:
                if len(s) > 1:
                # put the letter back to the string:
                    s_new += pairs[0]
                else:
                    eliminated.append(pairs[0])
            else:
                if ord(pairs[0]) > ord(pairs[1]):
                    #keep pairs[0]
                    print(f"1st letter {pairs[0]} comes after 2nd letter {pairs[1]}")
                    eliminated.append(pairs[1])
                    s_new += pairs[0]
                elif ord(pairs[0]) == ord(pairs[1]):
                    #keep pairs[1]
                    print("letters are equal")
                    eliminated.append(pairs[0])
                    s_new += pairs[1]
                else:
                    print(f"2nd letter {pairs[1]} comes after 1st letter {pairs[0]}")
                    eliminated.append(pairs[0])
                    s_new += pairs[1]
            # if i % 2 == 0:
            #     eliminated.append(s[i])
            #     if i == 0:
            #         s = s[n+1:]
            #     else:
            #         s = s[:n-1] + s[n+1:]
            #     print(s)
            if s_new != '':
                print(f"Input string is updated to: {s_new}")
            else:
                print("Input string is now empty")
        s = s_new
        print(f"s is updated to {s}")

    return eliminated

s = "BCAAB"

print(compare_pairs(s))

def compare_pairs_submitted(s):

    eliminated = []
    
    while s != '':
        n = len(s)
        s_new = ''
        for i in range(0, n, 2):
            if i + 1 == n:
                pairs = [s[i]]
            else:
                pairs = [s[i], s[i + 1]]

            if len(pairs) == 1:
                if len(s) > 1:
                    s_new += pairs[0]
                else:
                    eliminated.append(pairs[0])
            else:
                if ord(pairs[0]) > ord(pairs[1]):
                    eliminated.append(pairs[1])
                    s_new += pairs[0]
                elif ord(pairs[0]) == ord(pairs[1]):
                    eliminated.append(pairs[0])
                    s_new += pairs[1]
                else:
                    eliminated.append(pairs[0])
                    s_new += pairs[1]
        s = s_new

    return eliminated

''' Exercise 2
Imagine a medieval tournament where knights participate in jousting matches. The knights are arranged in a circular formation (represented as an array in your program), 
and each knight is initially assigned strength, represented as integers from 1 to 100, determined randomly.

The game consists of rounds. On each round, each knight fights the knight on his right side by subtracting the strength of his opponent from his own. Since this is a circular game, 
the knight on the right side of the last knight in the array is the first knight. Note that all matches are played in parallel, so the strengths are updated only after all matches 
are played. If after a match, a knight's strength becomes equal to or less than zero, symbolizing the knight's defeat, the knight is removed from the game in the next round.

The game continues until a situation develops in which no more moves can be made. This happens either when there is just one knight standing or all remaining knights have equal 
strength meaning no knight can win a match.

Given the list of knights' strengths in the initial order, your program should calculate the number of rounds in the tournament.'''

def tournament(knights):
    rounds = 0

    while True:
        rounds += 1
        print(f"Round {rounds}:")
        print("-" * 100)
        print(f"Evaluating knights: {knights}")
        print()
        n = len(knights)
        first, second = 0, 0
        matches = []

        for i in range(n):
            if i+1 == n:
                print(f"Evaluating knight[{i}]: {knights[i]} v knight[0]: {knights[0]}")
                matches.append(knights[i] - knights[0])
                print(f"Updated knights[{i}]: {matches[i]}")
            else:
                print(f"Evaluating knight[{i}]: {knights[i]} v knight[{i + 1}]: {knights[i + 1]}")
                first = knights[i] - knights[i + 1]
                
                #print(f"Updated knights[{i}]: {matches[i]}")
                #print(f"Updated knights[{i + 1}]: {matches[i + 1]}")
                matches.append(first)
                #matches.append(second)
                print(f"Matches array updates TBD: {matches}")

        print(f"Matches array consists of: {matches}")

        print("Eliminating elements with values <= 0")
        matches = [x for x in matches if x > 0]
        print(f"Updated matches array: {matches}")

        print(f"Assigning matches array to knights array before looping")
        knights = matches[:]
        print(f"Updated knights: {knights}")

        if len(knights) <= 1:
            
            print("We've reached the end")
            return rounds
        elif len(set(knights)) == 1:
            rounds += 1
            return rounds
        
        matches.clear()
        print(f"Round {rounds} end")
        print("*" * 100)



test = [100, 50, 30, 20]
# test = [70, 80, 60]
#test = [30, 20, 10, 40, 50]
#test = [100]
print(tournament(test))

def tournament_submitted(knights):
    rounds = 0

    while True:
        if len(knights) <= 1:
            return rounds
        rounds += 1
        n = len(knights)
        first, second = 0, 0
        matches = []

        for i in range(n):
            if i+1 == n:
                #print(f"Evaluating knight[{i}]: {knights[i]} v knight[0]: {knights[0]}")
                matches.append(knights[i] - knights[0])
                #print(f"Updated knights[{i}]: {matches[i]}")
            else:
                #print(f"Evaluating knight[{i}]: {knights[i]} v knight[{i + 1}]: {knights[i + 1]}")
                first = knights[i] - knights[i + 1]
                #second = -first
                #print(f"Updated knights[{i}]: {matches[i]}")
                #print(f"Updated knights[{i + 1}]: {matches[i + 1]}")
                matches.append(first)
                #matches.append(second)


        matches = [x for x in matches if x > 0]

        knights = matches[:]

        if len(knights) <= 1:
            return rounds

        elif len(set(knights)) == 1:
            rounds += 1
            return rounds
        
        matches.clear()

''' Exercise 3
In a unique town, there's a popular game that involves the town's houses and their numbers. What's special about this town is that each house is sequentially numbered from 1 to n. 
The game is played based on an interesting rule regarding these house numbers.

At each step of the game, every house number must "donate" one of its digits to the house on its right (or to the first house in the case of the last house). 
The particular digit to be transferred in each step is determined by the current game step: during the i-th step, the i-th digit from the right of each house number (1-indexed) is 
transferred. If a house number doesn't have the specified number of digits for a step, it doesn't donate any digit in that step.

During the transfer, the chosen digit is removed from its position in the donor house number and then added to the front (leftmost side) of the receiving house number. 
All numbers change simultaneously.

The function, house_game(houses), should simulate each step of the game, starting from transferring the rightmost (1st digit) and proceeding one digit position towards the left 
in each successive step, until there is no change in the house numbers from one step to the next. It should return the sequence of house numbers at the end.

It is guaranteed that there are at least two houses and there is no digit 0 in the numbers.

For instance, if houses = [123, 234, 345, 456], the function performs as follows:

Step 1 -> Transfer the 1st digit from the right (rightmost digit):

    Before Transfer:
        House 1: 123
        House 2: 234
        House 3: 345
        House 4: 456

    Digit Transfer:
        Transfer '3' from House 1 to the front of House 2
        Transfer '4' from House 2 to the front of House 3
        Transfer '5' from House 3 to the front of House 4
        Transfer '6' from House 4 to the front of House 1

    After Transfer: [612, 323, 434, 545]

Step 2 -> Transfer the 2nd digit from the right:

    Before Transfer:
        House 1: 612
        House 2: 323
        House 3: 434
        House 4: 545

    Digit Transfer:
        Transfer '1' from House 1 to the front of House 2
        Transfer '2' from House 2 to the front of House 3
        Transfer '3' from House 3 to the front of House 4
        Transfer '4' from House 4 to the front of House 1

    After Transfer: [462, 133, 244, 355]

Step 3 -> Transfer the 3rd digit from the right (leftmost digit):

    Before Transfer: [462, 133, 244, 355]

    After Transfer: [362, 433, 144, 255]

In Step 4, no further changes occur, so the final output is [362, 433, 144, 255].

This sequence of transformations leads to the final set of house numbers, [362, 433, 144, 255].
'''

def house_game(houses):

    n = len(houses)
    step = 0
    houses = [str(h) for h in houses]
    donor = ''
    receiver = ''
    house_address_remainder = ''

    while True:
        
        new_houses = houses.copy()
        
        for i in range(n):           
           if len(houses[i]) >= step+1: # does the house have enough digits?
            print(f"i: {i} of n: {n} | House: {houses[i]} | step: {step}")
            digit = houses[i][-(step+1)]
            if step == 0:
                house_address_remainder = new_houses[i][:-(step+1)]
            else:
                house_address_remainder = new_houses[i][:-(step+1)] + new_houses[i][-(step):]
            #print(f"House [{i}]: {houses[i]} | digit: {digit} | remainder of address: {house_address_remainder}")
            receiver = digit + new_houses[(i + 1) % n]
            print(f"i: {i} House: {houses[i]} digit: {digit} donor: {house_address_remainder} receiver: {receiver}")
            #new_houses[(i + 1) % n] = digit + houses[(i + 1) % n][:-1]
            #new_houses[(i + 1) % n] = digit + houses[(i + 1) % n][:-(step + 1)] + new_houses[(i + 1) % n][-step:]
            new_houses[(i + 1) % n] = receiver
            new_houses[i] = house_address_remainder
            #print(f"House {(i + 1) % n} {houses[(i + 1) % n]} vs New House {(i +1) % n} {new_houses[(i + 1) % n]}")
            print(f"Houses: {houses}")
            print(f"New Houses {new_houses}")
        

        if new_houses == houses:
            break
        houses = new_houses
        print(houses)
        #print(f"New houses array: {new_houses}")
        step += 1
    houses = [int(h) for h in houses]
    return houses

houses = [123, 234, 345, 456]
houses = [141, 4]

print(house_game(houses))

''' advice:
Nice effort! You’re close, but there are a few things to fix:

    houses should be a list of strings, not a list of integers.
    new_houses = str(houses.copy()) makes a single string, not a list—use houses.copy() instead.
    When you do houses[i][i+1], that’s not the right index. To get the ii-th digit from the right, use houses[i][-(step+1)].
    You need to build up new_houses as a list, updating each house after all removals and insertions are calculated.

Try starting with:

Python
houses = [str(h) for h in houses]

and use a variable like step to track which digit to move. Can you try updating your loop with these ideas?
'''

def house_game_submitted(houses):

    n = len(houses)
    step = 0
    houses = [str(h) for h in houses]
    receiver = ''
    house_address_remainder = ''

    while True:
        
        new_houses = houses.copy()
        
        for i in range(n):           
           if len(houses[i]) >= step+1: # does the house have enough digits?
            digit = houses[i][-(step+1)]
            if step == 0:
                house_address_remainder = new_houses[i][:-(step+1)]
            else:
                house_address_remainder = new_houses[i][:-(step+1)] + new_houses[i][-(step):]
            receiver = digit + new_houses[(i + 1) % n]
            new_houses[(i + 1) % n] = receiver
            new_houses[i] = house_address_remainder

        if new_houses == houses:
            break
        houses = new_houses
        step += 1

    houses = [int(h) for h in houses]
    return houses