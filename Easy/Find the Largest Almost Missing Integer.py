class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        if k == 1:
            return max((num for num in nums if counter[num] == 1), default=-1)
        
        if k == len(nums):
            return max(nums)
        
        answer = [-1]
        left, right = nums[0], nums[-1]
        if counter[left] == 1:
            answer.append(left)
        if counter[right] == 1:
            answer.append(right)
        
        return max(answer)
