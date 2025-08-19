class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = cur_count = 0
        for num in nums:
            if num == 0:
                cur_count += 1
                count += cur_count
            else:
                cur_count = 0
        return count
