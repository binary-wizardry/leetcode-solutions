class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter = [0] * 10 ** 5 + [0]
        for cost in costs:
            counter[cost] += 1
        
        number = 0
        costs = chain.from_iterable(repeat(cost, count) for cost, count in enumerate(counter) if count)
        for cost in costs:
            coins -= cost
            if coins < 0:
                break
            number += 1
        
        return number
