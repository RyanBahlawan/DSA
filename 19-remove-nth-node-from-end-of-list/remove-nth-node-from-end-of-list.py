# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0,head)
        
        l = dummy
        r = head
        count = 0

        while r and n!=count:
            r = r.next
            count+=1

        while r:
            l = l.next
            r = r.next
        
        delete = l.next
        temp = l.next.next
        l.next = temp
        delete.next = None
        return dummy.next