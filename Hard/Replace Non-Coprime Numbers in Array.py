class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and (div := gcd(stack[-1], num)) > 1:
                prev = stack.pop()
                num = prev * num // div
            stack.append(num)
        return list(stack)
