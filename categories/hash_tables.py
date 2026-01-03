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

# TESTS
# nums = [2, 7, 11, 15]
# target = 9

# nums = [3, 2, 4]
# target = 6

# nums = [3, 8, 12, 3]
# target = 6

# print(two_sum(nums, target))

# FIND THE FIRST NON-REPEATING CHAR IN STR
'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

EXAMPLE 1:
    Input: s = "leetcode"
    Output: 0
    Explanation: 'l' is the first character and it only appears once.
    
EXAMPLE 2:
    Input: s = "loveleetcode"
    Output: 2
    Explanation: 'l' appears twice. 'o' appears twice. 'v' is the first unique character.

EXAMPLE 3:
    Input: s = "aabb"
    Output: -1
'''

def first_unique_char(s: str) -> int:
    # return the index of the first unique char in str
    # if none, return -1

    char_counter = {}

    # count char occurences and store in the dict
    for char in s:
        # if the char is not in the dict, update counter to 1
        if char not in char_counter:
            char_counter[char] = 1
        # if it's there, increment the value to the key by 1
        else:
            char_counter[char] += 1
    
    # look for the first non-repeating char
    for key, value in char_counter.items():
        # the first key that contains 1 as a value is the non-repeating char
        if value == 1:
            # find the index of the current key in the string
            return s.find(key) # <- .find() can be time expensive

    # if there's no unique char in the str
    return -1



# TESTS
# s = "leetcode" # -> 0
#Explanation: 'l' is the first character and it only appears once.

# s = "loveleetcode" # -> 2
#Explanation: 'l' appears twice. 'o' appears twice. 'v' is the first unique character.

# s = "aabb" # -> -1

# print(first_unique_char(s))

# ALTERNATIVE SOLUTION
def first_unique_char_alternative(s: str) -> int:
    # return the index of the first unique char in str
    # if none, return -1

    char_counter = {}

    # count char occurences and store in the dict
    for char in s:
        # if the char is not in the dict, update counter to 1
        if char not in char_counter:
            char_counter[char] = 1
        # if it's there, increment the value to the key by 1
        else:
            char_counter[char] += 1
    
    # (OPTIMAL VERSION)
    # loop through str returning index and char
    for index, char in enumerate(s):
        # pass the char as a key in the dictionary
        # check if equals to 1
        # if so, return the referent index of this char from str
        if char_counter[char] == 1:
            return index

    # if there's no unique char in the str
    return -1

s = "loveleetcode" # -> 2
print(first_unique_char_alternative(s))

# SENIOR APPROACH WITH COUNTER MODULE (By Gemini)
from collections import Counter

def first_unique_char(s: str) -> int:
    """
    Finds the index of the first non-repeating character.
    Time Complexity: O(n)
    Space Complexity: O(1) (technically O(26) or O(k) unique chars)
    """
    # 1. Build frequency map
    # Counter does the loop and counting for you instantly
    count = Counter(s) 
    
    # 2. Find the first index where count is 1
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    
    return -1