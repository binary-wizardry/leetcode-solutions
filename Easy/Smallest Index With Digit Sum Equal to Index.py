class Solution:
    @staticmethod
    def digit_sum(n):
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total
    
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == self.digit_sum(num):
                return i
        return -1
