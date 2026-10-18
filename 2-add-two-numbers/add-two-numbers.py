# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummy = ListNode(0,None)
        head = dummy

        while l1 and l2:
            sum = carry+l1.val+l2.val
            if sum>=10:
                carry = 1
                dummy.next = ListNode(sum%10,None)
            else:
                dummy.next = ListNode(sum,None)
                carry = 0
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        if not l2 and l1:
            while l1:
                sum = carry+l1.val
                if sum>=10:
                    carry = 1
                    dummy.next = ListNode(sum%10,None)
                else:
                    dummy.next = ListNode(sum,None)
                    carry = 0
                dummy = dummy.next
                l1 = l1.next

        if not l1 and l2:
            while l2:
                sum = carry+l2.val
                if sum>=10:
                    carry = 1
                    dummy.next = ListNode(sum%10,None)
                else:
                    dummy.next = ListNode(sum,None)
                    carry = 0
                dummy = dummy.next
                l2 = l2.next

        if carry:
            dummy.next = ListNode(1, None)
        
        return head.next
