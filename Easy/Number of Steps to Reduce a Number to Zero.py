class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            num = num - 1 if num % 2 else num // 2
            steps += 1
        return steps

# just simulate the process
