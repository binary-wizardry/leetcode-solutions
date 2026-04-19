class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        result = 0
        
        while j < len(nums2) and i < len(nums1):
            num1, num2 = nums1[i], nums2[j]

            if i == j or num1 <= num2:
                result = max(result, j - i)
                j += 1
            else:
                i += 1
        
        return result
