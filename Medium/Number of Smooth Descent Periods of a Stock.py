class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = cur = 0
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                cur += 1
                count += cur
            else:
                cur = 0
        return count + len(prices)
