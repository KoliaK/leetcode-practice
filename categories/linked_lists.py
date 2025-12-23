# REVERSE A SINGLY LINKED LIST
'''
given the head of a singly linked list
reverse the list, and return the reversed list

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
'''
# NODE CLASS
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# MY SOLUTION
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr is not None:
    # assign next value as value that is after current value
        next_node = curr.next
    # reconnect current next value as the prev value
        curr.next = prev
    # advance previous value to become current value
        prev = curr
    # current value becomes next value
        curr = next_node

        # == in short ==
        # curr.next -> prev
        # prev -> curr
        # curr -> curr.next

    return prev

# SENIOR APPROACH WITH TUPLE UNPACKING
def reverse_list_pythonic(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr is not None:
        # curr.next -> prev
        # prev -> curr
        # curr -> curr.next
        curr.next, prev, curr == prev, curr, curr.next
    
    return prev

# FAST AND SLOW POINTER TO FIND THE MIDDLE OF A LIST
# (Floyd's Cycle Finding Algorithm or "Tortoise and Hare")
'''
given the head of a singly linked list,
return the middle node.
if there are two middle nodes (even number of items),
return the second middle node.

Example 1 (Odd): 1 -> 2 -> 3 -> 4 -> 5 Middle: 3
Example 2 (Even): 1 -> 2 -> 3 -> 4 -> 5 -> 6 Middle: 4
'''

def middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head

    # while fast is not None and fast.next is not None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# LINKED LIST CYCLE DETECTION CODE
def is_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    # while fast is not None and fast.next is not None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # if slow points to the same object as fast: return True
        if slow is fast:
            return True
    return False

# MERGE TWO LINKED LISTS
'''
You are given the heads of two sorted linked lists: 
-list1
-list2.
Merge them into one sorted list and return 
the head of the new list.

Example:
    list1: 1 -> 2 -> 4
    list2: 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
'''

def merge_two_sorted(list1: ListNode, list2: ListNode) -> ListNode:
    # create a dummy node to avoid complex if/else
    # it can store any value, since we will never use it
    # the dummy guarantees there is always a node to attach to.
    dummy = ListNode(-1)
    tail = dummy

    # iterate while both lists have nodes remaining
    while list1 and list2:
        # compare values to see which one is smaller
        if list1.val < list2.val:
            # attach list1's node to our chain
            tail.next = list1
            # advance list1 forward
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        
        # always move the tail forward
        # so it's ready for the next attachment
        tail = tail.next
    
    # cleanup
    # one list is now empty, but the other still has nodes
    # since they are sorted, we can just attach the remainder instantly
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    # return the start of the list (skipping the dummy anchor)
    return dummy.next