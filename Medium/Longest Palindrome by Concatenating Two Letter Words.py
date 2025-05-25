class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = Counter()
        count = 0
        
        for a, b in words:
            if b + a in hashmap and hashmap[b + a] > 0:
                count += 4
                hashmap[b + a] -= 1
            else:
                hashmap[a + b] += 1

        for a, b in hashmap:
            if a == b and hashmap[a + b] > 0:
                return count + 2
        return count
