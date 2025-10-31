class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        while nums[i] == i:
            i += 1
        a = nums[i]
        while nums[i] == i - 1:
            i += 1
        b = nums[i]
        return [a, b]
