# FIND NUMBERS WITH EVEN NUMBER OF DIGITS
'''
Given an array nums of integers, return how many of them contain an even number of digits.

EXAMPLE 1:
    Input: nums = [12, 345, 2, 6, 7896]
    Output: 2
    Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
    Therefore, only 12 and 7896 contain an even number of digits.
EXAMPLE 2:
    Input: nums = [555, 901, 482, 1771]
    Output: 1
    Explanation:
    Only 1771 contains an even number of digits.
'''

def find_numbers(nums: list[int]) -> int:
    # this function returns how many numbers
    # on the list have an EVEN number of digits

    counter = 0

    # loop through every number transforming
    # them into strings so I can split and count
    # how many digits
    for num in nums:
        int_to_str = str(num)
        
        if len(int_to_str) % 2 == 0:
            counter += 1
    return counter

# tests
nums = [12, 345, 2, 6, 7896] # -> 2
# nums = [555, 901, 482, 1771] # -> 1

# print(find_numbers(nums))
