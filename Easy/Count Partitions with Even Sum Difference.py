class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            num = nums[1]
            left += num
            right -= num
            if (right - left) % 2 == 0:
                count += 1
        return count
