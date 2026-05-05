# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            tail = head
        else:
            return head
        
        n = 1
        while tail and tail.next:
            tail = tail.next
            n += 1
        
        k = k % n
        tail = head
        for _ in range(k):
            tail = tail.next

        new_tail = head
        while tail.next:
            new_tail, tail = new_tail.next, tail.next

        tail.next = head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
