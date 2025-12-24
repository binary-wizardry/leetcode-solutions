class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        count = 0
        capacity.sort(reverse=True)
        while apples > 0:
            apples -= capacity[count]
            count += 1
        return count
