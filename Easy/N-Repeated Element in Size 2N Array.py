class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashtable = set()
        for num in nums:
            if not num in hashtable:
                hashtable.add(num)
            else:
                return num
