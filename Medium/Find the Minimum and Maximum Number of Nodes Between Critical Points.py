# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticals, i = [], 1
        
        while head.next and head.next.next:
            prev, cur, next = head, head.next, head.next.next
            
            if prev.val < cur.val > next.val or prev.val > cur.val < next.val:
                criticals.append(i)
            i += 1
            head = head.next
        
        if len(criticals) < 2:
            return [-1, -1]
        
        min_distance = min(b - a for a, b in pairwise(criticals))
        max_distance = criticals[-1] - criticals[0]
        return [min_distance, max_distance]
