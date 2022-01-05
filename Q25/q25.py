from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        truhead = head
        prev_tail = None
        section_head = head
        current_index = 0
        while head != None:
            if current_index%k == 0 and current_index!=0:
                next_in_line = section_head.next
                prev_node = section_head
                for i in range(k-1):
                    cn = next_in_line
                    next_in_line = next_in_line.next
                    cn.next = prev_node
                    prev_node = cn
                section_head.next = next_in_line
                if prev_tail != None:
                    prev_tail.next = cn
                else:
                    truhead = cn
                prev_tail = section_head
                section_head = head
            head = head.next
            current_index += 1
        if current_index%k == 0 and current_index!=0:
            next_in_line = section_head.next
            prev_node = section_head
            for i in range(k-1):
                cn = next_in_line
                next_in_line = next_in_line.next
                cn.next = prev_node
                prev_node = cn
            section_head.next = next_in_line
            if prev_tail != None:
                prev_tail.next = cn
            else:
                truhead = cn
            prev_tail = section_head
            section_head = head
        return truhead