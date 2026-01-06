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
    # them into strings so I can count
    # how many digits they got using len()
    for num in nums:
        int_to_str = str(num)
        # for each string which length divided by two
        # returns the remainder as zero, increment counter 
        if len(int_to_str) % 2 == 0:
            counter += 1
    return counter

# tests
# nums = [12, 345, 2, 6, 7896] # -> 2
# nums = [555, 901, 482, 1771] # -> 1

# print(find_numbers(nums))

# MAX CONSECUTIVE ONES
'''
Given a binary array nums (containing only 0s and 1s), return the maximum number of consecutive 1s in the array.

EXAMPLE 1:
    Input: nums = [1, 1, 0, 1, 1, 1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
EXAMPLE 2:
    Input: nums = [1, 0, 1, 1, 0, 1]
    Output: 2
'''

def max_consecutive(nums: list[int]) -> int:
    current_streak = 0
    max_streak = 0

    # for every number I need to verify if it's 1 or 0
    # if it's 1, increment current_streak
    for index, value in enumerate(nums):

        # if the current element is 1
        if value == 1:
            current_streak += 1
            # compares and updates max_streak
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak

# tests
# nums = [1, 1, 0, 1, 1, 1] # -> expected 3
# nums = [1, 0, 1, 1, 0, 1] # -> expected 2
# nums = [0, 0, 1, 1, 1, 0]# -> expected 3
# print(max_consecutive(nums))

# RUNNING SUM OF 1D ARRAY
'''
Given an array nums, we define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

EXAMPLE 1:
    Input: nums = [1, 2, 3, 4]
    Output: [1, 3, 6, 10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
EXAMPLE 2:
    Input: nums = [3, 1, 2, 10, 1]
    Output: [3, 4, 6, 16, 17]

You need to create a new list (or modify the existing one) where every element is the sum of itself plus the one before it.
'''

# return a list where each num is the result of
# a sum between current and all the previous numbers

def running_sum(nums: list[int]) -> list[int]:
    # for each index and value in nums
    for i, v in enumerate(nums):
        # if it's the first element, keep it as it is
        if i == 0:
            nums[i] = v
        # otherwise, increment the current value
        # to the previous value in the list itself
        else:
            nums[i] += nums[i-1]
    # return the refactored list
    return nums

nums = [1, 2, 3, 4] # -> expected [1, 3, 6, 10]
# nums = [3, 1, 2, 10, 1] # -> expected [3, 4, 6, 16, 17]
print(running_sum(nums))

# SENIOR APPROACH (By Gemini)
def runningSum(nums: list[int]) -> list[int]:
    # Start from the 2nd element (index 1) to the end
    for i in range(1, len(nums)):
        # Add the previous sum to the current element
        nums[i] += nums[i - 1]
    return nums

# or simply
from itertools import accumulate

def runningSum(nums: list[int]) -> list[int]:
    return list(accumulate(nums))