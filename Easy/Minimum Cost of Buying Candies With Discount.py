class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        result, i = 0, 0
        
        while i < len(cost) - 2:
            result += cost[i] + cost[i + 1]
            i += 3
        
        if i == len(cost) - 1:
            result += cost[i]
        elif i == len(cost) - 2:
            result += cost[i] + cost[i + 1]

        return result
