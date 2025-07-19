class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            path = result[-1]
            cur = folder[i]
            if not cur.startswith(path) or cur[len(path)] != '/':
                result.append(cur)
        return result
