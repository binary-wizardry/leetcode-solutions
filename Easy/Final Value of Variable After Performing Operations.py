class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        increments = decrements = 0
        for operation in operations:
            if '+' in operation:
                increments += 1
            else:
                decrements += 1
        return 0 + increments - decrements
