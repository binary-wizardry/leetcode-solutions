class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left = max_length = 0
        
        for right, char in enumerate(s):
            counter[char] += 1
            
            while counter[char] > 2:
                counter[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
