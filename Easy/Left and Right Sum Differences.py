class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = list(accumulate(nums, initial=0))[:-1]
        rightSum = reversed(list(accumulate(reversed(nums), initial=0)))
        next(rightSum)
        return [abs(a - b) for a, b in zip(leftSum, rightSum)]
