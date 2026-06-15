# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = mid = tail = head
        
        while tail and tail.next:
            tail = tail.next.next
            if prev != mid:
                prev = prev.next
            mid = mid.next

        prev.next = mid.next
        return head if prev != mid else None
