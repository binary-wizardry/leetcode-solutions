class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return 'none'
        match len(set(nums)):
            case 1: return 'equilateral'
            case 2: return 'isosceles'
            case 3: return 'scalene'
