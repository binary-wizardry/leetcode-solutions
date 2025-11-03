class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left, right = 0, 1
        time = 0
        while right < len(colors):
            if colors[left] == colors[right]:
                if neededTime[left] > neededTime[right]:
                    time += neededTime[right]
                    right += 1
                else:
                    time += neededTime[left]
                    left, right = right, right + 1
            else:
                left, right = right, right + 1
        return time
