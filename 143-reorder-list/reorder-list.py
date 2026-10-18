# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        prev = slow
        slow = slow.next
        prev.next = None
        while slow != None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        curr = head
        while curr!=prev and curr.next!=prev:
            temp1 = curr.next
            curr.next = prev
            temp2 = prev.next
            prev.next = temp1
            prev = temp2
            curr = temp1