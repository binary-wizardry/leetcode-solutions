class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        count = i = 0
        for num in arr1:
            while i < len(arr2) - 1 and abs(arr2[i + 1] - num) <= abs(arr2[i] - num):
                i += 1
            if abs(arr2[i] - num) > d:
                count += 1
        return count
