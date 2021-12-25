from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        truhead = head
        cur_index = 0
        prev_node = None
        prev_prev_node = None
        while head != None:
            if cur_index % 2 == 0:
                prev_node = head
                head = head.next
            else:
                next_in_line = head.next
                if cur_index == 1:
                    truhead = head
                    head.next = prev_node
                    prev_node.next = next_in_line
                else:
                    prev_prev_node.next = head
                    head.next = prev_node
                    prev_node.next = next_in_line
                prev_prev_node = prev_node
                head = next_in_line
            cur_index += 1
        return truhead