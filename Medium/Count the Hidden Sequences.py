class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = mn = mx = 0 
        for diff in differences:
            n += diff
            if n < mn:
                mn = n
            elif n > mx:
                mx = n
        size = mx - mn
        return max(upper - lower - size + 1, 0)
