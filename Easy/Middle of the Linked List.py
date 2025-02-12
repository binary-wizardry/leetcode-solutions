# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = end = head
        while end and end.next:
            end = end.next.next
            middle = middle.next
        return middle

# use two pointers
