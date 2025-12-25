class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        count = 0
        for i in range(k):
            count += max(happiness[i] - i, 0)
        return count
