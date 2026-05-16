class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 , len(nums) - 1
        while left < right:
            while nums[left] == nums[right] and left < right:
                left += 1
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
