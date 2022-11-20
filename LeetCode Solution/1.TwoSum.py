class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx

"""
=> def twoSum(self, nums: List[int], target: int) -> List[int]:
        Python has introduced type hinting, 
        which mean we could hinting the type of variable, 
        this was done by doing variable: type (or parameter: type), 
        so for example target is a parameter, of type integer.

        the arrow (->) allows us to type hint the return type, 
        which is a list containing integers.

=> for idx, value in enumerate(nums):
        Example:
            l1 = ["eat", "sleep", "repeat"]
            for count, ele in enumerate(l1):
                print(count)
                print(ele)
            output:
                0
                eat
                1
                sleep
                2
                repeat
        
        Syntax: 
            enumerate(iterable, start=0)
        Parameters:
            Iterable: any object that supports iteration
            Start: the index value from which the counter is to be started, 
                   by default it is 0
"""