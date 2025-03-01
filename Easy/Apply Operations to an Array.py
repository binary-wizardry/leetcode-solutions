class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # simulate all operations
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        # moving zeros to the end 
        zeros_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_count += 1
            else:
                nums[i - zeros_count] = nums[i]
        return nums[:-zeros_count] + [0] * zeros_count if zeros_count else nums
