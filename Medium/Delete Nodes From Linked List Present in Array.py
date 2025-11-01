# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head.val in nums:
            head = head.next
        cur = head
        while cur: 
            while cur.next and cur.next.val in nums:
                cur.next = cur.next.next
            cur = cur.next
        return head
