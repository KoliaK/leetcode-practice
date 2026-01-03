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
# print(first_unique_char_alternative(s))

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

# INTERSECTION OF TWO ARRAYS
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

EXAMPLE 1:
    Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]
EXAMPLE 2:
    Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    Output: [9, 4] (or [4, 9])
'''
# loop approach
def array_intersection(arr_a: list[int], arr_b: list[int]) -> list[int]:
    # transform arrays in sets
    # to handle duplicates
    arr_a = set(arr_a)
    arr_b = set(arr_b)
    
    # whatever the numbers that are present
    # in both sets will be stored here
    result = []

    # for every number in A
    for i in arr_a:
        # if also in B
        if i in arr_b:
            # push to the result list
            result.append(i)
    return result
        
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# Output: [2]


nums1 = [4, 9, 5] 
nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4] (or [4, 9])

# print(array_intersection(nums1, nums2))

# set operator approach
def array_set_intersection(arr_a: list[int], arr_b: list[int]) -> list[int]:
    arr_a = set(arr_a)
    arr_b = set(arr_b)

    # return everything that is in both sets
    '''
    A & B = return everything in common
        (intersection)
    A - B = return everything from A that is NOT in B
        (difference)
    B - A = return everything from B that is not in A
        (difference)
    A ^ B = return everything that is NOT in common
        (symmetric difference)
    '''
    return list(arr_a & arr_b)
        
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# Output: [2]


nums1 = [4, 9, 5] 
nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4] (or [4, 9])

# print(array_set_intersection(nums1, nums2))

# GROUP ANAGRAMS
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Note: An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

EXAMPLE 1:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]
EXAMPLE 2:
    Input: strs = [""]
    Output: [[""]]
'''

def group_anagrams(strs: list[str]) -> list[str]:
    # must group the anagrams in arr together
    # ['cat', 'dog', 'god'] => ['cat', ['dog', 'god']]
    result = [] # this will group anagrams together
    anagrams = {} # this will store the anagrams GROUPS in keys

    # for each word in arr
    for word in strs:
        # sort the word and join together
        # this will be the dict keys
        sorted_word = ''.join(sorted(word))
        # if the sorted word (key) is not in the dict
        if sorted_word not in anagrams:
            # create a key with the sorted word
            # and store the original word as a value
            anagrams[sorted_word] = [word]
        # if the key is already in the dict
        else:
            anagrams[sorted_word].append(word)
    
    # push to result each value (group of words) 
    # that belong to the same key
    for value in anagrams.values():
        result.append(value)
    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# returns [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# print(group_anagrams(strs))

# SENIOR SOLUTION using defaultdict (By Gemini)
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups anagrams using sorted string as the key.
    Time Complexity: O(N * K log K) where N is number of strings, K is max length of a string.
    Space Complexity: O(N * K)
    """
    # defaultdict(list) means: "If key is missing, create an empty list []"
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Create the key (same as you did)
        key = "".join(sorted(word))
        
        # No need for 'if/else' checks!
        anagram_map[key].append(word)
        
    # Return the values directly cast to a list
    return list(anagram_map.values())

