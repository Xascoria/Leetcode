from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        prev_tail = None
        truhead = tranverse_node = head
        for i in range(left-1):
            prev_tail = tranverse_node
            tranverse_node = tranverse_node.next

        rev_end = tranverse_node
        prev_rev_node = None
        next_in_line = None
        for i in range(right-left):
            prev_rev_node = tranverse_node
            if next_in_line == None:
                tranverse_node = tranverse_node.next
            else:
                tranverse_node = next_in_line
            next_in_line = tranverse_node.next

            tranverse_node.next = prev_rev_node

        if prev_tail != None:
            prev_tail.next = tranverse_node
        else:
            truhead = tranverse_node
        rev_end.next = next_in_line
        return truhead