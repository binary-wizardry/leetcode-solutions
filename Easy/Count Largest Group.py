class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter(sum(int(d) for d in str(num)) for num in range(1, n + 1))
        most_common = groups.most_common()[0][1]
        return sum(1 for count in groups.values() if count == most_common)
