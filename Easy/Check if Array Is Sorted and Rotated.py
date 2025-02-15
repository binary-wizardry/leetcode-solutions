class Solution:
    def check(self, nums: List[int]) -> bool:
        rotate_flag = 0
        for index in range(len(nums) - 1):
            if nums[index + 1] < nums[index]:
                rotate_flag += 1
                if nums[0] <  nums[-1] or rotate_flag == 2:
                    return False
        return True
