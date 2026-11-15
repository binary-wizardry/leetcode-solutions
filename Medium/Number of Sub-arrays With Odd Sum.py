class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = even = 0
        count = 0 
        for prefix in accumulate(arr):
            if prefix % 2:
                count += 1 + even
                odd += 1
            else:
                count += odd
                even += 1
        return count % (10 ** 9 + 7)
