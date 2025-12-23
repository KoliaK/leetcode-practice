# BEST TIME TO BUY AND SELL STOCK O(n)
'''
Buy at the cheapest price.
if no stock has been bought yet, 
the first best price is day 1's or infinity.
compare the current_cheapest with the next price.
If price < current_cheapest, update current_cheapest.

The next step is to find the max_profit.
current_profit = price - current_cheapest
if current_profit > max_profit
max_profit = current_profit
outside the loop, return the highest possible profit (int)
return max_profit
'''

def highest_profit(prices: list[int]) -> int:
    # if the list is empty
    if not prices:
        return False
    # min_price can also be set to float('inf')
    min_price = prices[0]
    current_profit = 0
    max_profit = 0

    for price in prices:
        # time to buy cheaper
        if price < min_price:
            min_price = price
        # time to sell and set profit
        else:
            current_profit = price - min_price
        
        # check for higher profit
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit

# print(highest_profit([7, 1, 5, 3, 6, 4])) # => 5
# print(highest_profit([7, 6, 4, 3, 1])) # => 0

# SENIOR SOLUTION FOR THE SAME PROBLEM
def highest_profit_senior(prices: list[int]) -> int:
    # no need to check if the list is empty at the start
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # update min_price found so far
        if price < min_price:
            min_price = price

        # calculate profit and update max_profit in one clean step
        # use max() to return the highest value without an extra 'if'
        else:
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
    return max_profit

# print(highest_profit_senior([7, 1, 5, 3, 6, 4])) # => 5
# print(highest_profit_senior([7, 6, 4, 3, 1])) # => 0

# OR SIMPLY
def highest_profit_no_if_else(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # compares current price with min_price so far
        min_price = min(price, min_price)
        # compares max_profit with current profit (price - min_price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# print(highest_profit_no_if_else([7, 1, 5, 3, 6, 4])) # => 5
# print(highest_profit_no_if_else([7, 6, 4, 3, 1])) # => 0

# =========================================================== #

# CONTAINS DUPLICATE
'''
returns true if any value appears twice
in an array, and false if every element is distinct

my solution is to transform the array in a set
to automatically handle duplicates, and compare the length
of the set with the original list.

return true if they have different sizes.
'''

# SENIOR SOLUTION O(n)
def contains_duplicate(nums: list[int]) -> bool:
    set_nums = set(nums)
    return len(set_nums) != len(nums)

# print(contains_duplicate([1, 2, 3, 1])) # => True
# print(contains_duplicate([1, 2, 3])) # => False
# print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # => True

# CONTAINS DUPLICATE O(n log n) slower, but saves memory
def contains_duplicate_lighter(list: list[int]) -> bool:
    # sort the list to ensure duplicates will be next to each other
    sorted_list = sorted(list)
    # we must verify if the current index value is equals
    # to the previous index
    for index in range(1, len(sorted_list)):
        if index == 0:
            continue
        elif sorted_list[index] == sorted_list[index - 1]:
            return True
    return False

# print(contains_duplicate_lighter([1, 5, 2, 4, 3, 1])) # => True
# print(contains_duplicate_lighter([1, 5, 2, 4, 3])) # => False

# =========================================================== #

# PRODUCT OF ARRAY EXCEPT SELF
'''
given an integer array of nums return an array answer
such that answer[i] is equal to the product of all the 
elements of nums except nums[i]

Must be O(n)

Cannot use the division operation
(i.e. multiply everything and divide by nums[i])

Example:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
# Explanation:
# Index 0: 2*3*4 = 24
# Index 1: 1*3*4 = 12
# Index 2: 1*2*4 = 8
# Index 3: 1*2*3 = 6

My solution:
I'd slice the list and multiply everything 
to the left of i
to the right of i
multiply left and right
append to a new list for each iteration

it's necessary to handle if 
left_slice == None or right_slice == None
to avoid breaking the loop for an "out of index" error.

this would fail since I'd be 
slicing O(n) and multiplying O(n) the same list => O(n²)

'''

def left_products(nums: list[int]) -> list[int]:
    result = []
    previous_value = 1
    previous_product = 1

    # iterate through indexes
    for index in range(len(nums)):
        if index == 0:
        # on nums[0], just append 1 to result
        # since there's nothing to multiply with
        # mathematically, anything multiplied by "nothing" is 1
            result.append(1)
        else:
            # for every other number, multiply all the previous numbers
            # so current index is not included, 
            # then we get the previous number
            previous_value = nums[index - 1]
            # if we are at index3 (1) 
            # previous_value = 4
            # previous_product = 2 
            # (since we multiplied every number to the left so far) 
            # 4 * 2 = 8
            new_value = previous_value * previous_product
            # update previous_product to the new_value because we are
            # accumulating the product of each previous number
            previous_product = new_value
            result.append(previous_product)
    return result

# NOW SAME THING BUT REVERSE
def right_products(nums: list[int]) -> list[int]:
    result = []
    previous_value = 1
    previous_product = 1

    # loop from the last index to the first index in reverse
    # start at len(nums)-1 otherwise out of range error
    # stop at -1 index which in this case means:
    # "include the first index"
    # step -1 for reverse iteration
    for index in range(len(nums)-1, -1, -1):
        if index == len(nums)-1:
            result.append(1)
        else:
            previous_value = nums[index + 1]
            new_value = previous_value * previous_product
            previous_product = new_value
            result.append(previous_product)
    result.reverse()
    return result

# ALTOGETHER
def product_except_self(nums:list[int]) -> list[int]:
    left_list = left_products(nums)
    right_list = right_products(nums)

    final_answer = []

    for i in range(len(nums)):
        val = left_list[i] * right_list[i]
        final_answer.append(val)
    return final_answer

# SENIOR SOLUTION (no need to create 2 lists or 2 functions)
def product_except_senior(nums: list[int]) -> list[int]:
    length = len(nums)
    # prefilled list (if len(list) == 4 -> [1, 1, 1, 1])
    answer = [1] * length

    # left pass starts at [->, _, _, _]
    # start the loop at index 1, so the previous index is 0
    # starts at index 1 because this avoids
    # dealing with out of range error (no if i == 0 needed)
    for i in range(1, length):
        # multiplies whatever comes before current index
        # from answer (always 1) and nums
        # updates current index for ANSWER
        # does that for every iteration ignoring i itself
        answer[i] = answer[i-1] * nums[i-1]
    
    # right pass starts at [_, _, _, <-]
    # the acc represents the product of everything 
    # to the right of current index
    right_accumulator = 1
    # run through the list entirely, but reversed
    # start at last index (len-1 because out of range error)
    # stop at -1 (the end), but steps reversed (-1)
    # so index -1 is actually 0
    for i in range(length-1, -1, -1):
        # multiplies current index of answer by the acc
        answer[i] *= right_accumulator
        # multiplies current index of nums by the acc
        right_accumulator *= nums[i]
        # this loop doesn't need to ignore the current index
        # nums[i] only updates the accumulator to be used
        # on the NEXT iteration
    return answer


# print(left_products([2, 4, 1, 3])) # => [1, 2, 8, 8]
# 2 becomes because anything times "nothing" = [1]
# 4 has only the number 2 to the left, so becomes [2]
# 1 has 2 and 4 to the left, so 4 * 2 = [8]
# 3 has 2, 4, 1 to the left, so 2 * 4 * 1 = [8]

# print(right_products([2, 4, 1, 3])) # => [12, 3, 3, 1]

# FINAL TESTS
# print(product_except_self([1, 2, 3, 4])) # => [24, 12, 8, 6]
# print(product_except_self([-1, 1, 0, -3, 3])) # => [0, 0, 9, 0, 0]
# print(product_except_self([0, 4, 0])) # => [0, 0, 0]

print(product_except_senior([1, 2, 3, 4])) # => [24, 12, 8, 6]
# print(product_except_senior([-1, 1, 0, -3, 3])) # => [0, 0, 9, 0, 0]
# print(product_except_senior([0, 4, 0])) # => [0, 0, 0]

# =========================================================== #