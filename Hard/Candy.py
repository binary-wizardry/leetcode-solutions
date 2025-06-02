class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [0] * n, [0] * n

        cur = 0
        for i, (a, b) in enumerate(pairwise(ratings), 1):
            if b > a:
                cur += 1
                left[i] = cur
            else:
                cur = 0
        
        cur = 0
        for i, (a, b) in enumerate(pairwise(reversed(ratings)), 1):
            if b > a:
                cur += 1
                right[i] = cur
            else:
                cur = 0

        return sum(1 + max(l, r) for l, r in zip(left, reversed(right)))
      
