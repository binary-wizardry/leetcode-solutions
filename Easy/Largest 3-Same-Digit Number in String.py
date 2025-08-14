class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ['']
        for _, group in groupby(num):
            group = ''.join(group)
            if len(group) >= 3:
                result.append(group[:3])
        return sorted(result)[-1]
