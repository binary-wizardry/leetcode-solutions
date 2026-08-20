class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums = iter(nums)
        arr1, arr2 = [next(nums)], [next(nums)]
        for num in nums:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        return arr1 + arr2
