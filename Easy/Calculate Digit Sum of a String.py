class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = ''.join(map(str, (sum(map(int, batch)) for batch in batched(s, k))))
        return s
