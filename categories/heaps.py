# Kth LARGEST ELEMENT IN AN ARRAY (TOP K PATTERN)
r'''
Given an integer array nums and an integer k, return the k^th largest element in the array.

Note that it is the k^th largest element in the sorted order, not the k^th distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2 Output: 5 Reasoning: Sorted, the array is [1,2,3,4,5,6]. The 2nd largest is 5.

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints: 1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''
# this is time O(n log n) because of .sort() (timsort)
# space complexity O(1) for sorting in place without creating a new list
def kth_largest_element(arr : list[int], k : int) -> int:
    # it must return the largest Kth element in the sorted order

    # first, ensure that list is sorted
    # since the original list isn't needed, .sort() for memory saving
    # sorted() function copies the list to reorganize it
    arr.sort()
    
    # now, I need to verify what's the largest number based on K
    # if the list is [1,2,3,4] and k == 2 -> return arr[-2] (3)
    k = k * -1 # transform k into a negative number
    # return the Kth index from the sorted list in reverse
    return arr[k]


# print(kth_largest_element([3,2,1,5,6,4], 2))

# SAME PROBLEM BUT WITH MIN-HEAP APPROACH
import heapq # use O(log n) insertion/deletion procedures on priority queues

def min_heap_largest_element(nums : list[int], k : int) -> int:
    # initialize an empty heap
    heap = []
    
    for num in nums:
        if len(heap) < k:
            # if the heap hasn't reached size k, just push
            heapq.heappush(heap, num)
        else:
            # if heap is full, push the new num, and pop the smallest
            # ONLY if he new num is larger than the smallest in the heap
            heapq.heappushpop(heap, num)
    # return final heap after the loop
    return heap[0]

# print(min_heap_largest_element([3,2,1,5,6,4], 2))

# SAME PROBLEM WITH QUICK SELECT APPROACH
# because we ignore half the array at every step (on average)
# time drops from O(n log n) to O(n) on average

def partition(nums : list[int], left: int, right: int) -> int:
    # all smaller will be on the left of the pivot
    # all larger to the right
    # pivot is placed exactly in its correct sorted position
    # return the index where the pivot ended up
    pivot = nums[right] # pick rightmost element as pivot
    p_index = left # this pointer remembers where the next 'smaller' goes

    # iterate from left to right
    for index in range(left, right):
        # if a number is <= pivot, swap it with nums [p_index]
        if nums[index] <= pivot:
            nums[index], nums[p_index] = nums[p_index], nums[index]
            # increment p_index
            p_index += 1
        
    # swap the pivot (nums[right]) with nums[p_index]
    # to put the pivot in the middle
    nums[right], nums[p_index] = nums[p_index], nums[right] 
    return p_index

def quickselect(nums : list[int], left : int, right : int, k_smallest_index : int) -> int: 
    # if list contains only one element
    if left == right:
        return nums[left]
    
    # get the pivot index from partition
    pivot_index = partition(nums, left, right)

    if pivot_index == k_smallest_index:
        return nums[pivot_index]
    elif pivot_index < k_smallest_index:
        return quickselect(nums, pivot_index + 1, right, k_smallest_index)
    else:
        return quickselect(nums, left, pivot_index - 1, k_smallest_index)

def find_kth_largest(nums : list[int], k : int) -> int:
    target_index = len(nums) - k
    return quickselect(nums, 0, len(nums) - 1, target_index)

# tests
def run_tests():
    print("Running tests...")
    
    # Test 1: Standard case (unsorted)
    # Sorted: [1, 2, 3, 4, 5, 6]. 2nd largest is 5.
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5, "Test 1 Failed"
    
    # Test 2: Array with duplicates
    # Sorted: [1, 2, 2, 3, 3, 4, 5, 5, 6]. 4th largest is 4.
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4, "Test 2 Failed"
    
    # Test 3: k = 1 (Largest element)
    assert find_kth_largest([10, 20, 5], 1) == 20, "Test 3 Failed"
    
    # Test 4: k = len(nums) (Smallest element)
    assert find_kth_largest([10, 20, 5], 3) == 5, "Test 4 Failed"
    
    # Test 5: Negative numbers
    assert find_kth_largest([-1, -2, -3, -4], 2) == -2, "Test 5 Failed"
    
    print("✅ All tests passed!")

# run_tests()

# SENIOR SOLUTION (PROVIDED BY GEMINI)
import random

def find_kth_largest_senior(nums: list[int], k: int) -> int:
    """
    Finds the kth largest element using Iterative QuickSelect with Randomization.
    Time Complexity: O(N) average, O(N^2) worst case (rare).
    Space Complexity: O(1)
    """
    # Target index in a sorted array (0-indexed)
    k = len(nums) - k # convert "2nd largest" to "index 4"
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # 1. Randomization: Pick a random pivot index and swap it to the end
        # This prevents O(N^2) performance on sorted arrays
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        # 2. Partition (Lomuto Partition Scheme)
        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[right], nums[p] = nums[p], nums[right]
        
        # 3. Decision (Iterative narrowing)
        if p == k:
            return nums[p]
        elif p < k:
            left = p + 1  # Move window to the right
        else:
            right = p - 1 # Move window to the left
    # Safety Net. If someone passes invalid inputs
    # return -1 instead of return None
    # -1 convention basically means "element not found"        
    return -1
