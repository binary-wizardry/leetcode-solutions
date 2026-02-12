class Solution:
    def longestBalanced(self, s: str) -> int:
        max_length = 0
        n = len(s)

        for i in range(n):
            counter = [0] * 26

            for j in range(i, n):
                c = s[j]
                counter[ord(c) - ord('a')] += 1
                if len(set(filter(None, counter))) == 1:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
