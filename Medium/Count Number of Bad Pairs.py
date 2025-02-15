class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        hash_table = {}
        # counting good pairs 
        # j - i = nums[j] - nums[i] is the same as i - nums[i] = j - nums[j]
        # so count elements with the same difference between number and nidex
        for i in range(n):
            hash_table[nums[i] - i] = hash_table.get(nums[i] - i, 0) + 1
        pairs = n * (n - 1) // 2  # total number of pairs
        good_pairs = sum(n * (n - 1) // 2 for n in hash_table.values())

        return pairs - good_pairs
