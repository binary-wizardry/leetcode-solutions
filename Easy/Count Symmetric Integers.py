class Solution:
  def countSymmetricIntegers(self, low: int, high: int) -> int:
    def isSymmetricInteger(num: int) -> bool:
      if num >= 10 and num <= 99:
        return num // 10 == num % 10
      if num >= 1000 and num <= 9999:
        left = num // 100
        right = num % 100
        return left // 10 + left % 10 == right // 10 + right % 10
      return False

    return sum(isSymmetricInteger(num) for num in range(low, high + 1))


# just for fun
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(sum(map(int, n[:len(n) // 2])) == sum(map(int, n[len(n) // 2:])) for n in map(str, range(low, high + 1)) if not len(n) % 2)
