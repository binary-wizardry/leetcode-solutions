class Solution:
    def sumDigits(self, num: int) -> int:
        result = 0
        while num != 0:
            result += num % 10
            num //= 10
        return result


    def maximumSum(self, nums: List[int]) -> int:
        hash_table = {}
        for n in nums:
            key = self.sumDigits(n)
            hash_table.setdefault(key, []).append(n)
            hash_table[key] = sorted(hash_table[key], reverse=True)[:2]  # save two max numbers with same sum of digits
        max_sum = -1
        for pair in hash_table.values():
            if len(pair) == 2:
                max_sum = max(max_sum, sum(pair))
        return max_sum
