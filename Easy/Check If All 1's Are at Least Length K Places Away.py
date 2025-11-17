class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -inf
        for i in range(len(nums)):
            if nums[i]:
                if i - prev > k:
                    prev = i
                else:
                    return False
        return True
