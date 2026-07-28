class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        
        left_part = []
        for i, char in enumerate(ascii_lowercase):
            count = counts[i] // 2
            for _ in range(count):
                left_part.append(char)
        left_part = ''.join(left_part)
        
        mid = ''
        for i, char in enumerate(ascii_lowercase):
            if counts[i] % 2:
                mid = char
                break
        
        return left_part + mid + left_part[::-1]
