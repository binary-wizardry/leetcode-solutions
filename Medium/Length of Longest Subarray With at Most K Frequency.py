class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        length = left = 0
        
        for right, num in enumerate(nums):
            counter[num] += 1
            
            while counter[num] > k and left < right:
                counter[nums[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
        
        return length
