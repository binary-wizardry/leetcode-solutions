class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, lower_after = {}, {}
        upper, upper_after = {}, {}
        
        for letter in word:
            
            if letter.islower():
                lower[letter] = lower.get(letter, 0) + 1
                if letter.upper() in upper:
                    lower_after[letter] = lower_after.get(letter, 0) + 1
            
            elif letter.isupper():
                upper[letter] = upper.get(letter, 0) + 1
                if lower.get(letter.lower(), 0) > 0:
                    lower[letter.lower()] -= 1
                    upper_after[letter] = upper_after.get(letter, 0) + 1
        
        total = 0
        for letter, count in upper_after.items():
            if letter.lower() not in lower_after:
                total += 1
        
        return total
