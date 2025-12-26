# MOVING AVERAGE FROM DATA STREAM
'''
Scenario: Imagine you are building a monitoring tool that 
calculates the average CPU usage over the last n seconds. 
You receive a stream of integers (usage percentage), 
and you need to calculate the moving average of all integers 
in the sliding window of size size.

Requirements: 
Implement the MovingAverage class:
MovingAverage(int size): Initializes the object with the size of the window size.
double next(int val): Returns the moving average of the last size values of the stream.

Example:
movingAverage = MovingAverage(3)
movingAverage.next(1) # return 1.0 = ((1) / 1)
movingAverage.next(10) # return 5.5 = ((1 + 10) / 2)
movingAverage.next(3) # return 4.66667 = ((1 + 10 + 3) / 3)
movingAverage.next(5) # return 6.0 = ((10 + 3 + 5) / 3) -> Note: '1' fell out of the window.
'''

class MovingAverage:
    def __init__(self, size: int) -> None:
        self.size = size
        self.window = []

    def double_next(self, val : int) -> float:
        self.window.append(val)
        while len(self.window) <= self.size:
            return float(sum(self.window) / len(self.window))
        del self.window[0]
        return float(sum(self.window) / len(self.window))
        
    
# movingAverage = MovingAverage(3)
# movingAverage.double_next(1)
# movingAverage.double_next(10)
# movingAverage.double_next(3)
# print(movingAverage.double_next(8))

# SENIOR SOLUTION
# deque() allows popleft() in O(1) time
from collections import deque

class MovingAverageSenior:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def double_next(self, val : int) -> float:
        self.queue.append(val)
        
        self.window_sum += val

        if len(self.queue) > self.size:
            removed_val = self.queue.popleft()
            self.window_sum -= removed_val
        return self.window_sum / len(self.queue)
        
    
# movingAverageSenior = MovingAverageSenior(3)
# movingAverageSenior.double_next(1)
# movingAverageSenior.double_next(10)
# movingAverageSenior.double_next(3)
# print(movingAverageSenior.double_next(8))

# IMPLEMENT STACK USING QUEUES
'''
You need to implement a LIFO (Last-In-First-Out) Stack class, but you must strictly use FIFO (First-In-First-Out) Queues to build it.

In Python, you can use deque, but you are only allowed to use queue operations:

append() (push to back)
popleft() (peek/pop from front)
len() (size)

You cannot use pop() (which pops from the back) or index access [i].

Requirements: 
Implement the MyStack class:
void push(int x): Pushes element x to the top of the stack.
int pop(): Removes the element on the top of the stack and returns it.
int top(): Returns the element on the top of the stack.
boolean empty(): Returns true if the stack is empty, false otherwise.

Visualizing the Conflict:
Stack (Goal): You push 1, 2. If you pop, you expect 2.
Queue (Tool): You push 1, 2. If you popleft, you get 1.

Hint: How can you manipulate the queue so that the last thing you added becomes the first thing to come out?
'''

# deque already been imported in line 43
# allowed: append, popleft, len

class MyStack:
    def __init__(self):
        self.queue = deque()
        
    def void_push(self, val: int) -> None:
        # this function must append to the last index and rotate
        # (cannot use appendleft())
        self.queue.append(val)

        # rotate value (n-1) times, where n is the current len
        for index in range(len(self.queue) - 1):
            # remove from front
            reallocate_val = self.queue.popleft()
            # add to back
            self.queue.append(reallocate_val)

    def int_pop(self) -> int:
        # popleft() must remove the LAST index from
        # stack (rotate queue)
        error_message = 'Stack is empty. Cannot pop element.'
        return self.queue.popleft() if self.queue else error_message
        
    def int_top(self) -> int:
        # unpack the first value from stack
        # *_ means catch all remaining elements of the list
        # but ignore them all, except 'first_element'
        if self.queue:
            first_element, *_ = self.queue
            return first_element
        else:
            return 'Stack is empty. Cannot return the top element.'
        
    def boolean_empty(self) -> bool:
        # returns true if the list is empty
        # or return len(self.queue) == 0
        return not self.queue

# my_stack = MyStack()
# my_stack.void_push(1)
# my_stack.void_push(2)
# my_stack.void_push(3)
# print(my_stack.int_pop()) # -> expected to return 3!
# print(my_stack.int_top()) # -> expected to return 2 (3 has been poped)!
# print(my_stack.boolean_empty()) # -> expected to return False

# NUMBER OF RECENT CALLS
'''
You have a RecentCounter class which counts the number of 
recent requests within a certain time frame.

Requirements: 
Implement the RecentCounter class:

RecentCounter(): 
Initializes the counter with zero requests.

int ping(int t): 
Adds a new request at time t (milliseconds). Returns the number of requests that have happened in the past 3000 milliseconds (including the new request).

Constraint:
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call (time always moves forward).

Example:
counter = RecentCounter()
counter.ping(1)    # requests: [1], range: [-2999, 1], return: 1
counter.ping(100)  # requests: [1, 100], range: [-2900, 100], return: 2
counter.ping(3001) # requests: [1, 100, 3001], range: [1, 3001], return: 3
counter.ping(3002) # requests: [1, 100, 3001, 3002], range: [2, 3002], return: 3
                   # ^ Note: '1' is now older than 3000ms ago
                   # (3002 - 3000 = 2), so '1' drops off.

How would you use a Queue here?
When a new ping comes in, you add it.
Then, what do you check to decide what to remove?
(Think about the MovingAverage problem, but instead of checking len(queue) > size, what is your condition for removal?)
'''

class RecentCounter:
    def __init__(self):
        self.requests = deque() # this will receive the ping requests
        self.WINDOW_SIZE = 3000 # time limit in ms

    def ping(self, t : int) -> int:
        # this method returns the number of requests that
        # have happened in the past 3000 milliseconds
        # (including the new request)

        # time of request must be stored in self.requests
        # like [1, 15, 100] (116 ms used from the ms_window)
        self.requests.append(t)

        # loop logic
        # at self.requests[0] = 1
        # 1 < (1 - 3000) => 1 < -2999 ? False
        # 1 < (100 - 3000) => 1 < -2900 ? False
        # 1 < (3001 - 3000) => 1 < 1 ? False
        # 1 < (3002 - 3000) => 1 < 2 ? True
        # REMOVE from the queue so now [100, 3001, 3002]
        while self.requests[0] < (t - self.WINDOW_SIZE):
            self.requests.popleft()
        # return how many requests were made in the past 3000ms
        return len(self.requests)

# counter = RecentCounter()
# print(counter.ping(1))    # requests: [1], range: [-2999, 1], return: 1
# print(counter.ping(100))  # requests: [1, 100], range: [-2900, 100], return: 2
# print(counter.ping(3001)) # requests: [1, 100, 3001], range: [1, 3001], return: 3
# print(counter.ping(3002)) # requests: [1, 100, 3001, 3002], range: [2, 3002], return: 3
#                    # ^ Note: '1' is now older than 3000ms ago
#                    # (3002 - 3000 = 2), so '1' drops off.
            
