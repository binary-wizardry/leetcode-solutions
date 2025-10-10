class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[:k]
        for i in range(k, len(energy)):
            prev = dp[i % k]
            dp[i % k] = prev + energy[i] if prev > 0 else energy[i]
        return max(dp)
