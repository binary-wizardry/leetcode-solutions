class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices_by_nums = {}
        for i, num in enumerate(nums):
            indices_by_nums.setdefault(num, []).append(i)
        
        distance = float('inf')
        for indices in indices_by_nums.values():
            for i in range(len(indices) - 2):
                a, c = indices[i], indices[i + 2]
                distance = min(distance, c + c - a - a)
        
        return -1 if distance == float('inf') else distance
