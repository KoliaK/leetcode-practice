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