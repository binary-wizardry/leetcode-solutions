# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tail, mid = head.next, head
        while tail.next:
            tail = tail.next.next
            mid = mid.next
        
        prev, cur = mid, mid.next
        mid.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        
        tailhead = prev
        max_pair = 0
        while head:
            max_pair = max(head.val + tailhead.val, max_pair)
            head, tailhead = head.next, tailhead.next

        return max_pair
