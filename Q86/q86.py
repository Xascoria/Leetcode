from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = less_tail = None
        more_head = more_tail = None

        while head != None:
            if head.val < x:
                if less_tail == None:
                    less_head = head
                    less_tail = head
                else:
                    less_tail.next = head
                    less_tail = less_tail.next
            else:
                if more_tail == None:
                    more_head = head
                    more_tail = head
                else:
                    more_tail.next = head
                    more_tail = more_tail.next
            head = head.next
        if less_tail: less_tail.next = None
        if more_tail: more_tail.next = None
        if less_head == None:
            return more_head
        less_tail.next = more_head
        return less_head
