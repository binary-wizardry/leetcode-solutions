class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        for d in num:
            if d != '9':
                mx = num.replace(d, '9')
                break
        else:
            mx = num
        
        if num[0] != '1':
            mn = num.replace(num[0], '1')
        else:
            for d in num[1:]:
                if d not in '01':
                    mn = num.replace(d, '0')
                    break
            else:
                mn = num
        
        return int(mx) - int(mn)
