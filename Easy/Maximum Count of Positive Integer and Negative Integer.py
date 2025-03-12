class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        left = 0
        right = len(nums)
        index = right // 2
        guess = nums[index]
        while guess and right > left:
            if guess > 0 and nums[index - 1] < 0:
                break
            elif guess > 0:
                right = index - 1
            elif guess < 0:
                left = index + 1
            index = (left + right) // 2
            guess = nums[index]
        neg = nums[:index]
        pos = nums[index:]
        while neg and neg[-1] == 0:
            neg = neg[:-1]
        while pos and pos[0] == 0:
            pos = pos[1:]
        return max(len(neg), len(pos))
