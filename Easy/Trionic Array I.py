class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        increasing = False
        count = 0
        if nums[0] >= nums[1]:
            return False
        
        for a, b in pairwise(nums):
            if a == b:
                return False
            elif a < b and not increasing:
                count += 1
                increasing = True
            elif a > b and increasing:
                count += 1
                increasing = False

        return count == 3
