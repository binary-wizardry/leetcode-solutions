class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.extend(str(num))
        return list(map(int, answer))
