'''
8/15/2020

Two Sum Problem:

Given a list of numbers, and a target number, return the indicies of the TWO numbers that add up to the target number. If this does not exist, return -1, -1.

Input: [1, 2, 5, 7, 10], 11
Output: 0, 4

Please encapsulate this into a function. Watch out for edge cases...
'''

def two_sum(listnums:list, target:int) -> tuple:
    '''Takes a list of numbers and a target number, returns the indicies of the two numbers that add up to the target number. If not found return -1, -1'''
    for i in range(len(listnums)):
        to_find = target - listnums[i]
        if to_find in listnums:
            return i, listnums.index(to_find)
    return -1, -1

print(two_sum([1, 2, 5, 7, 10], 11))
