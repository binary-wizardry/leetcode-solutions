class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(n for n in nums if n)
        count = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                ab = nums[i] + nums[j]
                left, right = j + 1, n - 1
                while j + 1 <= left <= right:
                    mid = (left + right) // 2
                    c = nums[mid]
                    if c >= ab:
                        right = mid - 1
                    else:
                        left = mid + 1
                count += left - j - 1
        return count

# good solution
'''
        count = 0
        nums.sort()
        n = len(nums)
        for i in range(n-1, -1, -1):
            l, r = 0, i-1
            c = nums[i]
            while l < r:
                if nums[l] + nums[r] > c:
                    count += (r-l)
                    r -= 1
                else:
                    l += 1
        return count
'''
