class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # find all prime numbers <= right, using Sieve of Eratosthenes
        prime = []
        divisors = [0] * (right + 1)
        for i in range(2, right + 1):
            if divisors[i] == 0:
                divisors[i] = i
                prime.append(i)
            for p in prime:
                if p <= divisors[i] and p * i <= right:
                    divisors[p * i] = p
                else:
                    break
        # filter prime numbers that >= than left
        prime = [n for n in prime if n >= left]
        # find pair with minimum distance
        if len(prime) < 2:
            return [-1, -1]
        return min(itertools.pairwise(prime), key=lambda pair: pair[1] - pair[0])
