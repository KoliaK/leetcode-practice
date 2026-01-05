# SORT AN ARRAY
'''
Given an array of integers nums, sort the array in ascending order and return it.

The Constraint: You must implement the Quick Sort algorithm manually. Do not use Python's built-in sort() or sorted() functions.

EXAMPLE 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
EXAMPLE 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
'''

def sort_array(nums: list[int]) -> list[int]:

    # if the list is empty or have a single element
    if not nums or len(nums) == 1:
        return nums
    
    pivot = nums[0]

    # all the numbers smaller/larger than the pivot
    left = []
    right = []

    # for each number in the list, except the pivot
    for num in nums[1:]:
        if num < pivot:
            left.append(num)
            print(f'num added to left list {left}')
        else:
            right.append(num)
            print(f'num added to right list {right}')
    
    # recursive call with sublist left/right as argument
    # it will repeat until all the sublists are sorted
    # will return a list of [left nums, pivot, right nums]
    return sort_array(left) + [pivot] + sort_array(right)

# TESTS
# nums = [5,2,3,1] # -> [1,2,3,5]
nums = [5,1,1,2,0,0] # -> [0,0,1,1,2,5]
# print(sort_array(nums))

# SENIOR APPROACH WITH IN-PLACE QUICK SORT (By Gemini)
def quick_sort(nums: list[int]) -> list[int]:
    # Wrapper function to make the call simple
    def _quick_sort(items, start_index, end_index):
        # Base case: if the range is invalid or has 1 item
        if start_index >= end_index:
            return

        # 1. Partition the list and find where the Pivot landed
        pivot_index = partition(items, start_index, end_index)
        
        # 2. Recursively sort the left side
        _quick_sort(items, start_index, pivot_index - 1)
        
        # 3. Recursively sort the right side
        _quick_sort(items, pivot_index + 1, end_index)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums

def partition(nums, start, end):
    pivot = nums[end] # Pick the last element as the pivot
    wall = start      # "The Wall" starts at the beginning
    
    # 'current' acts as a scout exploring the list
    for current in range(start, end):
        if nums[current] < pivot:
            # We found a small number! 
            # Throw it behind the wall (swap)
            nums[wall], nums[current] = nums[current], nums[wall]
            
            # Move the wall forward one step
            wall += 1
            
    # Finally, put the pivot exactly ON the wall
    nums[wall], nums[end] = nums[end], nums[wall]
    
    # Return the location of the wall (this is the split point)
    return wall

