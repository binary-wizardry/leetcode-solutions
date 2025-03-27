class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        frequency = collections.Counter(nums)
        # most common element and his frequency in nums
        dominant, f = frequency.most_common(1)[0][0], frequency.most_common(1)[0][1]
        result = -1
        left, right = 0, f  # count dominant element in left and rigth slices
        for i in range(n - 1):
            item = nums[i]
            if item == dominant:
                left += 1
                right -= 1
                if left > (i + 1) // 2 and right > (n - i - 1) // 2:
                    result = i
                    break
        return result
