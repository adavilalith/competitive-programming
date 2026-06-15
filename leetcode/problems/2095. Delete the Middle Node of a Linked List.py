# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        slow=head
        fast=head.next
        prev=None
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
            if fast:
                fast=fast.next
        prev.next=slow.next
        return head