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

# n = 5
# print(climb_stairs(n))

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

# MIN COST CLIMBING STAIRS
'''
You are given an integer array cost where cost[i] is the cost of the i-th step on a staircase.

    -Once you pay the cost, you can either climb 1 or 2 steps.
    -You can either start from the step with index 0, or the step with index 1.
    -Return the minimum cost to reach the top of the floor (which is one step past the last index of the array).

Example 1:
    Input: cost = [10, 15, 20] Output: 15 
    Explanation:
        1. Start at index 1 (pay 15).
        2. Climb two steps to reach the top. Total cost = 15.
Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] Output: 6 Explanation: 
        Cheapest path: 
        Start at 0, then move to indices 2, 4, 6, 7, 9, then top. 1 + 1 + 1 + 1 + 1 + 1 = 6.
'''

def min_cost_climbing_stairs(cost: list[int]) -> int:
    # this will store the total accumulated price
    # to reach and step on index i
    dp = [0] * len(cost)
    # we always use the 2 previous values
    # to decide which one is cheaper
    dp[0] = cost[0]
    dp[1] = cost[1]

    # since we already know the 2 first values
    # loop from 2nd index further
    for i in range(2, len(dp)):
        # dp array (tabulation) update
        # every value from now on will be the
        # sum of current cost value + cheaper step
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # after the loop finishes, return the cheaper
    # last steps, since top is len(cost) not cost[-1]
    return min(dp[-1], dp[-2])
    
# cost = [10, 15, 20] # -> expected 15
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] # -> expected 6
# print(min_cost_climbing_stairs(cost))

# SENIOR SOLUTION (By Gemini)
def minCostClimbingStairs(cost: list[int]) -> int:
    # 1. Initialize the first two steps
    # We treat these variables as our "moving window" of history
    prev2 = cost[0]
    prev1 = cost[1]
    
    # 2. Iterate through the rest
    for i in range(2, len(cost)):
        # Calculate the cost for the current step
        current = cost[i] + min(prev1, prev2)
        
        # Shift the window forward
        prev2 = prev1
        prev1 = current
        
    # 3. The "Top" can be reached from the last step (prev1)
    #    or the second-to-last step (prev2)
    return min(prev1, prev2)

# HOUSE ROBBER
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, represented by an array nums.

The only constraint stopping you is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1, 2, 3, 1] Output: 4 
    Explanation: 
        Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4. Note: You cannot rob house 2 because it is adjacent to house 1.
Example 2:
    Input: nums = [2, 7, 9, 3, 1] Output: 12 Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.
'''

def house_robber(money: list[int]) -> int:
    # return the maximum ammount of money
    # without accessing 2 consecutive values

    prev2 = 0
    prev1 = 0

    for num in money:
        # is there more money in current house than the previous 2?
        current = max(prev1, num + prev2)

        prev2 = prev1
        prev1 = current
    return prev1

# SENIOR SOLUTION (By Gemini)
def rob(nums: list[int]) -> int:
    # 'rob' = max money if we rob the current house (requires coming from 2 steps back)
    # 'skip' = max money if we skip the current house (carries over previous max)
    
    rob_prev_prev = 0  # equivalent to your prev2
    rob_prev = 0       # equivalent to your prev1
    
    for loot in nums:
        # Option 1: Don't rob this house. We keep the max loot from the previous step.
        skip_house = rob_prev
        
        # Option 2: Rob this house. Add current loot to the safe loot from 2 steps ago.
        rob_house = loot + rob_prev_prev
        
        # The new max is whichever option yields more money
        current_max = max(skip_house, rob_house)
        
        # Shift our window forward
        rob_prev_prev = rob_prev
        rob_prev = current_max
        
    return rob_prev