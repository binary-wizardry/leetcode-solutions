class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            a, b = height[left], height[right]
            if a < b:
                if a * (right - left) > max_area:
                    max_area = a * (right - left)
                left += 1
            else:
                if b * (right - left) > max_area:
                    max_area = b * (right - left)
                right -= 1
        return max_area
