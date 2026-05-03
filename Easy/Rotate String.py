class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s, goal = deque(s), deque(goal)
        for _ in goal:
            if s == goal:
                return True
            s.rotate(-1)
        return False

''' 
best solution (not my)
    
res = s + s
if goal in res:
    return True 
return False

'''
