class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise_or = reduce(operator.or_, nums)
        count = 1  # because maximum bitwise-OR is the bitwise-OR of the whole array and already counted
        for i in range(1, len(nums)):
            for subset in combinations(nums, i):
                count += reduce(operator.or_, subset) == max_bitwise_or
        return count

# it also has a nice backtracking recursive solution
