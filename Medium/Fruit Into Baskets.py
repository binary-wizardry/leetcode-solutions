class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        result = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit, 0) + 1
            while len(count) > 2:
                drop = fruits[left]
                count[drop] -= 1
                if not count[drop]:
                    del count[drop]
                left += 1
            result = max(result, right - left + 1)
        return result
