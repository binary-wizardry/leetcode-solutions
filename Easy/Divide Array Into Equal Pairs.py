class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_table = set()
        for n in nums:
            if n in hash_table:
                hash_table.remove(n)
            else:
                hash_table.add(n)
        return not hash_table
