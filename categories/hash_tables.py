# TWO SUM
'''
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

EXAMPLE 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

EXAMPLE 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]
'''

def two_sum(arr: list[int], target: int) -> list[int]:
    seen_map = {}

    for index, num in enumerate(arr):
        difference = target - num
        if difference in seen_map:
            return [seen_map[difference], index]
        else:
            seen_map[num] = index

        
# nums = [2, 7, 11, 15]
# target = 9

# nums = [3, 2, 4]
# target = 6

nums = [3, 8, 12, 3]
target = 6

print(two_sum(nums, target))