class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for n1, n2, n3 in itertools.combinations(arr, 3):
            if abs(n1 - n2) <= a and abs(n2 - n3) <= b and abs(n3 - n1) <= c:
                count += 1
        return count

# brute force with enumeration all triplets
