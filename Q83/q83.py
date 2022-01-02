from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        output_head = output_tail = head
        start = head.next
        while start != None:
            if start.val != output_tail.val:
                output_tail.next = start
                output_tail = output_tail.next
            start = start.next
        if output_tail != None: output_tail.next = None
        return output_head