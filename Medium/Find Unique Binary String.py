class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # convert the given strings into base 10 integers    
        hash_table = set(int(n, 2) for n in nums)
        # just iterate through all possible binary strings of the required length until we find the missing one
        for combo in itertools.product('01', repeat=len(nums)):
            binary_string = ''.join(combo)
            if int(binary_string, 2) not in hash_table:
                return binary_string
