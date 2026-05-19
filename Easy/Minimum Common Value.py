class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0
                
        while p1 < len(nums1) and p2 < len(nums2):
            a, b = nums1[p1], nums2[p2]
            
            if a == b:
                return a
            elif a < b:
                p1 += 1
            else:
                p2 += 1
        
        return -1
