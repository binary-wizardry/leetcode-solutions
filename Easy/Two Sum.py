class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if hashmap.get(num) is not None:
                return [hashmap[num], index]
            hashmap[target - num] = index

# use a hash map to store the difference [target - num]
