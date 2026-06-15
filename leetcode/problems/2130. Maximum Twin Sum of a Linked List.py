# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        while fast:
            slow=slow.next
            fast=fast.next.next
        l=head
        r=slow
        a=[]
        b=[]
        res=0
        while r:
            a.append(l.val)
            b.append(r.val)
            l=l.next
            r=r.next
        b=b[::-1]
        for x,y in zip(a,b):
            res=max(res,x+y)
        return res