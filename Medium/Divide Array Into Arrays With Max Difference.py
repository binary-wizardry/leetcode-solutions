class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            a, b, c = nums[i: i + 3]
            if c - a > k:
                return []
            else:
                result.append([a, b, c])
        return result
