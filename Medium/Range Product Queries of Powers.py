class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers, power = [], 0
        while n:
            n, remainder = divmod(n, 2)
            if remainder:
                powers.append(power)
            power += 1
        # произведение степеней 2 равно 2^(сумма степеней)
        # поэтому считаем префиксную сумму
        prefix = list(accumulate(powers, initial=0))
        answers = [1 << (prefix[right + 1] - prefix[left]) for left, right in queries]
        # 1 << power = 2^power
        return [i % (10 ** 9 + 7) for i in answers]    
