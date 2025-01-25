# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        mov = head
        cnt = 0
        while (curr.next is not None):
            cnt += 1
            curr = curr.next
        indx = cnt - n - 1
        for i in range(indx):
            mov = mov.next
        if indx < 0:
            mov = None
        else:
            mov.next = mov.next.next
        return head
