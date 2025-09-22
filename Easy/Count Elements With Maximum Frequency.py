class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = [0] * 100
        for num in nums:
            frequency[num - 1] += 1
        max_freq = max(frequency)
        return max_freq * frequency.count(max_freq)
