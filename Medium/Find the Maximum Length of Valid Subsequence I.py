class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = odd_count = alternate_count = 0
        sign = 0 if nums[0] % 2 else 1
        
        for num in nums:
            if num % 2:
                odd_count += 1
            else:
                even_count += 1
            
            if sign % 2 ^ num % 2:
                alternate_count += 1
                sign = num

        return max(even_count, odd_count, alternate_count)
