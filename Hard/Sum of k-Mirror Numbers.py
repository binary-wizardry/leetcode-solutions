class Solution:
    def decimal_palindromes(self):  # this function from DeepSeek
        yield from range(1, 10)  # Сначала генерируем однозначные палиндромы
        length = 2
        while True:
            half_len = length // 2  # Определяем диапазон для "половинок"
            
            if length % 2 == 0:  # Четная длина
                start = 10 ** (half_len - 1)
                end = 10 ** half_len
                for n in range(start, end):
                    s = str(n)
                    yield int(s + s[::-1])
            
            else:  # Нечетная длина
                start = 10 ** half_len
                end = 10 ** (half_len + 1)
                for n in range(start, end):
                    s = str(n)
                    yield int(s + s[:-1][::-1])
            length += 1
    
    def is_palindrome(self, num: int, base: int):
        original, reverse = num, 0
        while num > 0:
            digit = num % base
            reverse = reverse * base + digit
            num //= base
        return original == reverse

    def kMirror(self, k: int, n: int) -> int:
        count, result = 0, 0
        decimal = self.decimal_palindromes()
        while count < n:
            num = next(decimal)
            if self.is_palindrome(num, k):
                count += 1
                result += num
        return result
