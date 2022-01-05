from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        truhead = None
        prev_tail = None
        cur_remove_val = -101
        while head != None and head.next != None:
            if head.next.val == cur_remove_val:
                head.next = head.next.next
                continue
            if head.val == cur_remove_val:
                head = head.next
                continue
            if head.val == head.next.val:
                cur_remove_val = head.val
                head.next = head.next.next
                continue
            nil = head.next
            if truhead == None:
                truhead = head
                prev_tail = truhead
                prev_tail.next = None
            else:
                prev_tail.next = head
                prev_tail = prev_tail.next
                prev_tail.next = None
            head = nil
        if head != None:
            if head.val != cur_remove_val:
                if prev_tail == None:
                    return head
                prev_tail.next = head
                head.next = None
        return truhead
