class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, low = 0, nums[0]
        for num in nums:
            if num - low > k:
                low = num
                count += 1
        return count + 1
