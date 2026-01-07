# CLIMBING STAIRS
'''
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

EXAMPLE 1:
    Input: n = 2 Output: 2 Explanation: There are two ways to climb to the top.
    - 1 step + 1 step
    - 2 steps
EXAMPLE 2:
    Input: n = 3 Output: 3 Explanation: There are three ways to climb to the top.

    - 1 step + 1 step + 1 step

    - 1 step + 2 steps

    - 2 steps + 1 step

CONSTRAINTS:
    1 <= n <= 45
'''

def climb_stairs(n: int) -> int:
    # this function must calculate how many ways
    # you can climb a staircase given the n value (steps)
    # rules: you can only climb 1 or 2 steps at a time
    # if n = 3 -> 1, 1, 1 or 1, 2 or 2, 1

    # prefill a list with n [0] elements
    fib_sequence = [0] * n
    
    for i in range(len(fib_sequence)):
        if i == 0:
            fib_sequence[i] = 1
        elif i == 1:
            fib_sequence[i] = 2
        else:
            # current number = sum of 2 previous values
            fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    
    # the last value reveals how many possibilities
    return fib_sequence[-1]

n = 5
print(climb_stairs(n))

# SENIOR APPROACH (By Gemini)
def climb_stairs(n: int) -> int:
    # Base cases to avoid loop logic for small numbers
    if n <= 2:
        return n
    
    # We only track the last two steps needed to calculate the next one
    prev2 = 1  # Originally step 1
    prev1 = 2  # Originally step 2
    
    # Start from step 3 up to n
    for _ in range(3, n + 1):
        # The new current step is the sum of the previous two
        current = prev1 + prev2
        
        # Shift our window forward for the next iteration
        prev2 = prev1
        prev1 = current
        
    return prev1