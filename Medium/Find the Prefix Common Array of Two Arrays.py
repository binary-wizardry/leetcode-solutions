class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        hash_A = set()
        hash_B = set()
        for i in range(len(A)):
            hash_A.add(A[i])
            hash_B.add(B[i])
            result.append(len(hash_A & hash_B))
        return result
