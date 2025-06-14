class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        max_d, min_d = '9', num[0]
        
        for d in num:
            if d != max_d:
                max_d = d
                break
        
        maximum = int(''.join(d if d != max_d else '9' for d in num))
        minimum = int(''.join(d if d != min_d else '0' for d in num))

        return maximum - minimum
        
