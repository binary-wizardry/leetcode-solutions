class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        count1, count2 = 0, 0

        for num in nums1:
            if not num:
                count1 += 1
                num = 1
            sum1 += num
                    
        for num in nums2:
            if not num:
                count2 += 1
                num = 1
            sum2 += num
        
        if (sum1 < sum2 and not count1) or (sum1 > sum2 and not count2):
            return -1
        
        return max(sum1, sum2)
