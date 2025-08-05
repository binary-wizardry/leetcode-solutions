class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for quantity in fruits:
            for i in range(len(baskets)):
                capacity = baskets[i]
                if quantity <= capacity:
                    baskets[i] = 0
                    break
            else:
                unplaced += 1
        return unplaced
