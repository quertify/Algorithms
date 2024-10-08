"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
"""
"""
choosing the DS : then I have to calculate all the time else maintain just a sum and divide it by the count
"""
class MovingAverage:
    def __init__(self, size:int) -> None:
        self.nums = []
        self.size = size
    def next(self, num:int) -> float:
        self.nums.append(num)
        window = self.size
        mov_sum = 0
        if self.size >= len(self.nums):
            window = len(self.nums)
        start = len(self.nums) - window
        end = len(self.nums)
        for i in range(start,end):
            mov_sum+=self.nums[i]
        avg = mov_sum / window
        print(avg)
        return avg
    
movingAverage = MovingAverage(3)
movingAverage.next(1)
movingAverage.next(10)
movingAverage.next(3)
movingAverage.next(5)
movingAverage.next(5)