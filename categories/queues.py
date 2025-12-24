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
        
    
movingAverageSenior = MovingAverageSenior(3)
movingAverageSenior.double_next(1)
movingAverageSenior.double_next(10)
movingAverageSenior.double_next(3)
print(movingAverageSenior.double_next(8))
