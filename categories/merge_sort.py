# MERGE SORT ARRAY
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Your Task: Merge nums2 into nums1 so that the resulting array is also sorted in non-decreasing order.

Constraints & Details:
1. The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

2. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored (they are placeholders).

3. nums2 has a length of n.

EXAMPLE:
    Input:
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Output:
    [1, 2, 2, 3, 5, 6]

(Note: The function does not return anything; it modifies nums1 in-place.)
'''

def merge_sort(nums1: list[int], nums2: list[int], m: int, n: int) -> None:
    # points to the last valid element in nums1 (not zero)
    p1 = m - 1
    # same, but for nums2
    p2 = n - 1
    # points to the end of nums1 array
    p_write = m + n - 1

    # while there are still items in nums2 to merge
    while p2 >= 0:
        # if p1 is valid and the value in nums1 is larger
        if (p1 >= 0) and (nums1[p1] > nums2[p2]):
            # write (copy) nums1 value to the end of nums1 
            nums1[p_write] = nums1[p1]
            # walks the pointer backwards
            p1 -= 1
        else:
            # write the nums2 value into nums1
            nums1[p_write] = nums2[p2]
            p2 -= 1
        p_write -= 1
    return
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge_sort(nums1, nums2, 3, 3)
print(nums1)
# expected to return [1, 2, 2, 3, 5, 6]