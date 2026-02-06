class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        nums.append(inf)
        right, count = 0, n
        for left, num in enumerate(nums):

            while nums[right] <= num * k and right < n:
                right += 1
            count = min(count, left + n - right)
        
        return count
