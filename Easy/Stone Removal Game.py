class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn_Alice = False
        k = 10
        while n >= k:
            n -= k
            k -= 1
            turn_Alice = not turn_Alice
        return turn_Alice
