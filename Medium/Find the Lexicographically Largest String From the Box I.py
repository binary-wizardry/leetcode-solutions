class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        length = n - numFriends + 1
        result = ''
        
        for i in range(n):
            cur = word[i: i + length]
            if cur > result:
                result = cur
        
        return result
