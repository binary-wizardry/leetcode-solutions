class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            even, odd = set(), set()

            for j in range(i, n):
                num = nums[j]
                if num % 2:
                    odd.add(num)
                else:
                    even.add(num)
                
                if len(even) == len(odd):
                    ans = max(ans, j - i + 1)
        
        return ans
