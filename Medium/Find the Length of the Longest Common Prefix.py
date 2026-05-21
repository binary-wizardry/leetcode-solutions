class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_hashtable = set()
        longest = 0

        for num in arr1:
            num = str(num)
            for i in range(1, len(num) + 1):
                prefix_hashtable.add(num[:i])

        for num in arr2:
            num = str(num)
            for i in range(1, len(num) + 1):
                if num[:i] in prefix_hashtable and i > longest:
                    longest = i
        
        return longest
