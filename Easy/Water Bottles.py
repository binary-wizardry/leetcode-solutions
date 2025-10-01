class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinkedBottles = 0
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            drinkedBottles += numBottles
            numBottles, emptyBottles = divmod(emptyBottles, numExchange)
            emptyBottles += numBottles
        return drinkedBottles + numBottles

'''
good solution
return numBottles + (numBottles - 1) // (numExchange - 1)
'''
