class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float('inf')
        prefix = list(accumulate(nums, initial=0))
        for length in range(l, r +  1):
            for i in range(length, len(prefix)):
                cur_sum = prefix[i] - prefix[i - length]
                if cur_sum > 0:
                    result = min(result, cur_sum)
        return result if result != float('inf') else -1
