"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:
TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
"""
class TwoSum():
    def __init__(self) -> None:
        self.nums = dict()

    def add(self, number:int) -> None:
        if number not in self.nums:
            self.nums[number] = 0
        self.nums[number]+=1

    def find(self, value:int) -> bool:
        for key, val  in self.nums.items():
            x = value - key
            if x in self.nums:
                if x!=key or self.nums[x] > 1:
                        return True
        return False
twoSum =  TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
twoSum.add(3)
print(twoSum.find(4))
print(twoSum.find(6))

"""
Establish a mapping between each number and the number of occurrences, 
and then traverse the HashMap. For each value, 
first find the difference t between this value and the target value, and then you need to look at it in two cases.

If the current value is not equal to the difference t, then return True as long as there is a difference t in the HashMap, or when the difference t is equal to the current value,
If the number of mapping times of the HashMap is greater than 1, it means that there is another number in the HashMap that is equal to the current value, and the addition of the two is the target value

"""