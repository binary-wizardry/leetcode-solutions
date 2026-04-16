class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        indexes_by_nums = {}
        for i, num in enumerate(nums):
            indexes_by_nums.setdefault(num, []).append(i)
        
        result = []
        l = len(nums)
        for query in queries:
            num = nums[query]
            indexes = indexes_by_nums[num]
            n = len(indexes)
            
            if n == 1:
                result.append(-1)
            else:
                i = bisect.bisect_left(indexes, query)
                left = indexes[i - 1]
                right = indexes[(i + 1) % n]
                distance = min(abs(left - query), abs(right - query), abs(l + query - left), abs(l - query + right))
                result.append(distance)

        return result
