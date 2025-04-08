class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hash_table = {}
        result = 0
        # iterate over triplets of elements
        for step, i in enumerate(range(0, len(nums), 3), 1):
            for num in nums[i:i + 3]:
                # if num is in the table, the value indicates the number of operations to remove it
                if num in hash_table:
                    result = max(hash_table[num], result)
                hash_table[num] = step
        return result
