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

# SAME PROBLEM, BUT WITH MIN-HEAP APPROACH
import heapq

def min_heap_largest_element(nums : list[int], k : int) -> int:
    # initialize an empty heap
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)
    return heap[0]

print(min_heap_largest_element([3,2,1,5,6,4], 2))