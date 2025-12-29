# RANGE SUM OF BST
r'''
The Challenge:
Given the root node of a binary search tree
and two integers low and high,
return the sum of values of all nodes
with a value in the inclusive range [low, high].

Example:
Input:
    Tree Structure: 
    Root = 10, 
    Left child = 5, 
    Right child = 15.

The 5 has children 3 and 7.
The 15 has a right child 18.

        10
       /  \
      5    15
     / \    \
    3   7    18

low = 7
high = 15

Logic:
    Node 10 is in range [7, 15]. (Keep it)
    Node 5 is less than 7. (Ignore it, but check children?)
    Node 15 is in range [7, 15]. (Keep it)
    Node 3 is less than 7. (Ignore)
    Node 7 is in range. (Keep it)
    Node 18 is greater than 15. (Ignore)
    
    Output: 32 (Because 10 + 15 + 7 = 32)

The Core Definition (BST Property):
Recall that for any node N:
All values in N.left < N.val
All values in N.right > N.val
'''

# how should the function behave?
'''
the function must compare node.val with low and high values to decide which way it moves:
if node.val < low -> skip and check right children
if node.val >= low and node.val <= high -> keep it and check left and right children
if node.val > high -> skip and check left children

keep track of kept values in a queue, pop values that are not in between low and high values
return sum(queue)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode usually forces you to implement the solution
# inside of a class for state management (avoiding name collisions, etc)
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        # if the root is none, return 0
        if root is None:
            return 0
        
        # check if root.val is < low ignore
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # check if root.val is > high ignore
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # if it's in the middle (valid), 
        # add root.val + results from children
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# tests

# build the tree
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)

# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)

# root.right.right = TreeNode(18)

# # instantiate the solution class
# sol = Solution()

# # if we want sum between 7 and 15.
# # expected nodes: 10, 15, 7. Sum = 32.
# result = sol.rangeSumBST(root, 7, 15)

# print(f"Calculated Sum: {result}")

# SEARCH IN A BST
'''
You are given the root of a BST and an integer val. Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return None.

Example:
Tree: Same as before (Root 10, Left 5, Right 15...)
Target val: 15

Output: You return the entire Node object for 15. (In the background, this includes the link to 18).
'''
# with recursion
def searchBST(root: TreeNode, target: int) -> TreeNode:
    if root is None:
        return None
    
    if target > root.val:
        return searchBST(root.right, target)
    elif target < root.val:
        return searchBST(root.left, target)
    else:
        return root.val

# with iteration
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    while root is not None:
        
        if root.val == val:
            return root
        
        elif val > root.val:
            root = root.right
        
        else:
            root = root.left
            
    # if the loop finishes, we hit a dead end (None).
    return None

# tests

# build the tree
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)

# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)

# root.right.right = TreeNode(18)

# # if the target is 15.
# # expected node to returm: 15
# result = searchBST(root, 15)

# print(f"Target node: {result}")

# VALIDATE BST
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

The Catch:It's not enough to just check if Left < Node < Right.

Example:
Root: 10
Right Child: 15
Right-Left Grandchild: 9
Is this valid? 

At node 15, the left child is 9. Since 9 < 15, that looks okay locally.
BUT: Node 9 is on the Right side of the main Root (10). Everything on the right side of 10 must be greater than 10.Since 9 < 10, this tree is Invalid.
'''

# root.right.left must be < than root.right but > root

def is_valid_BST(root: TreeNode) -> bool:
    # start with no limits (infinity)
    return node_validator(root, float('-inf'), float('inf'))

def node_validator(node: TreeNode, low: float, high: float) -> bool:

    # this time, we are not validating
    # if the node is empty
    if node is None:
        return True # <--- if hits the bottom, then it's a valid tree

    # if the current node is higher than
    # low and lower than high
    # if low > node.val > high:
    if not (low < node.val < high):
        return False
    
    # if left is valid, max limit becomes current node.val
    left_is_valid = node_validator(node.left, low, node.val)
    # if right is valid, min limit becomes current node.val 
    right_is_valid = node_validator(node.right, node.val, high)

    # return true ONLY if both sides are valid
    return left_is_valid and right_is_valid