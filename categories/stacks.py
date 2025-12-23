# VALID PARENTHESES
'''
Given a string s containing just the characters 
(, ), {, }, [, and ]
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''

def valid_parentheses(s: str) -> bool:
    stack = []

    parentheses_map = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    
    for i in s:
        # we found an open bracket
        if i in parentheses_map:
            stack.append(i)
        # we found a closing bracket
        else:
            # avoids a crash if the stack is empty
            if not stack:
                return False
            top_element = stack.pop()
            if parentheses_map[top_element] != i:
                return False

    return not stack

# SENIOR APPROACH
def senior_valid_parentheses(s: str) -> bool:
    bracket_map = {
        ')': '(', 
        ']': '[', 
        '}': '{'
    }

    stack = []

    for char in s:
        # if the character is a closing bracket
        if char in bracket_map:
            # pop the top element if stack is not empty
            # otherwise, assign a dummy value
            top_element = stack.pop() if stack else '#'

            # the mapped value (opener) must match the popped value
            if bracket_map[char] != top_element:
                return False
        else:
            # it's an opening bracket, push to stack
            stack.append(char)
    
    # if the stack is empty, all openers were closed correctly
    return not stack

# print(valid_parentheses('()['))
# print(senior_valid_parentheses('()['))

# REMOVE ALL ADJACENT DUPLICATES IN STRING

'''
You are given a string s consisting of lowercase English letters. A "duplicate removal" consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"

Explanation:
We match bb in "abbaca". Remove them -> "aaca".
Now we see aa in "aaca". Remove them -> "ca".
No more duplicates. Result is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
'''

def remove_adj_duplicates(s: str) -> str:
    stack = []
    
    for char in s:
        # Check if stack has items AND the top item matches current char
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)

print(remove_adj_duplicates('azxxzy')) # -> 'ay'

# MIN STACK
'''
The Challenge
Design a stack class that supports push, pop, top, and retrieving the minimum element in constant time.

You need to implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

The Catch: You must implement a solution with O(1) time complexity for each function.
'''

# the class must have the following methods:
# push(), pop(), top(), get_min()

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if min_stack is empty OR
        # val is smaller/equal to current min, push it
        # <= is necessary to handle duplicate minimums
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        min_value = self.stack.pop()

        if self.min_stack[-1] == min_value:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def get_min(self) -> int:
        return self.min_stack[-1]
    
# DAILY TEMPERATURES (Monotonic Stack)
'''
A monotonic stack is a stack where the elements are always sorted 
(either increasing or decreasing).

If you see a new number that breaks the order, 
you pop elements until the order is restored.

The Magic: The moment you pop an element 
is the moment you find the answer for that specific element.
=============================================================================
The Challenge
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the i-th day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0.

Example
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Breakdown of the Example:
Day 0 (73): Next warmer is Day 1 (74). Wait: 1 day.
Day 1 (74): Next warmer is Day 2 (75). Wait: 1 day.
Day 2 (75): Next warmer is Day 6 (76). Wait: 4 days.
Day 3 (71): Next warmer is Day 5 (72). Wait: 2 days.
...and so on.
'''

def daily_temperatures(temperatures: list[int]) -> list[int]:
    # answer is the number of days you have to wait
    # after the i-th day to get a warmer temp.
    # if there's no future day for which this is possible,
    # keep answer[i] == 0
    answer = [0] * len(temperatures)
    stack = [] # store days

    # we need to iterate through temperatures
    # while getting bot the index and the value
    for day, temp in enumerate(temperatures):
        # while stack is not empty (stack is True)
        # and temperature is higher than the temperature
        # of the last day stored in the stack
        while stack and temp > temperatures[stack[-1]]:
            # pop() not only removes the last element
            # it also returns WHAT was the element removed
            prev_day = stack.pop()
            # how many days passed
            answer[prev_day] = day - prev_day
        stack.append(day)
    return answer
