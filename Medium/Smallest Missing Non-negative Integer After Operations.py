class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = [0] * value
        for num in nums:
            counter[num % value] += 1
        
        number = 0
        while True:
            if counter[number % value] == 0:
                return number
            else:
                counter[number % value] -= 1
            number += 1
