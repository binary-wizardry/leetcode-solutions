class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, mid, right = 0, 0, len(nums) - 1
        
        while mid <= right:
            num = nums[mid]
            
            if num == 0:
                nums[left], nums[mid] = 0, nums[left]
                left += 1
                mid += 1
            
            elif num == 1:
                mid += 1
            
            else:
                nums[right], nums[mid] = 2, nums[right]
                right -= 1

# Dutch national flag problem
