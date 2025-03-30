class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        while s:
            index = 0
            end = s.rfind(s[index]) + 1  # end of part
            while index + 1 < end:
                index += 1
                # while letters from left part also are in the right part, move the border
                end = max(end, s.rfind(s[index]) + 1)  
            # divide into parts
            result.append(len(s[:end]))
            s = s[end:]
        return result
