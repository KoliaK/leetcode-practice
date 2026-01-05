# 1. The Class Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Your Solution Function
def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next

# --- TESTING HELPERS (The "Plumbing") ---

def create_linked_list(arr):
    if not arr:
        return None
    
    # 1. Manually create the HEAD (First node)
    head = ListNode(arr[0])
    current = head
    
    # 2. Loop through the REST of the items (skipping index 0)
    for val in arr[1:]:
        new_node = ListNode(val)
        current.next = new_node # Link previous node to new one
        current = new_node      # Move pointer forward
        
    return head

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# --- RUNNING THE TEST ---

# 1. Setup the input data
print("Test Case 1:")
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4])

print("Input List 1:", end=" ")
print_linked_list(l1)
print("Input List 2:", end=" ")
print_linked_list(l2)

# 2. Run your merge function
merged_head = merge_two_lists(l1, l2)

# 3. Print the result
print("Merged Result:", end=" ")
print_linked_list(merged_head)