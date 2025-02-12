class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = ['1']
        for num in range(2, n + 1):
            if not num % 3 and not num % 5:
                result.append('FizzBuzz')
            elif not num % 3:
                result.append('Fizz')
            elif not num % 5:
                result.append('Buzz')
            else:
                result.append(str(num))
        return result
      
