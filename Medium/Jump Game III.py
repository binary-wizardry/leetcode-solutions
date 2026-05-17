class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vizited = [False] * n
        vizited[start] = True
        q = deque((start, ))

        while q:
            i = q.popleft()
            
            if arr[i] == 0:
                return True

            for step in (i + arr[i], i - arr[i]):
                if 0 <= step < n and not vizited[step]:
                    vizited[step] = True
                    q.append(step)
        
        return False

# my BFS realization
# https://youtu.be/lbBpHdRmLzY
