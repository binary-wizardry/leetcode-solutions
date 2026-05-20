class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set1, set2 = set(), set()
        n = len(A)
        prefix = [0] * n
        
        for i in range(n):
            a, b = A[i], B[i]
            set1.add(a)
            prefix[i] += b in set1
            prefix[i] += a in set2
            set2.add(b)
        
        prefix = list(accumulate(prefix))
        return prefix
