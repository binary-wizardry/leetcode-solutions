class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        counter = Counter(nums)
        count = 0
        prev = defaultdict(int)
        for num in nums:
            if num:
                prev[num] += 1
                count += prev[num * 2] * (counter[num * 2] - prev[num * 2])
        zeros = nums.count(0)
        if zeros > 2:
            count += zeros * (zeros - 1) * (zeros - 2) // 6
        return count % MOD
