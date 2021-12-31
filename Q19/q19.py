from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tru_head = head
        cur_index = 0
        saved_node = None
        while head != None:
            head = head.next
            cur_index += 1
            if cur_index < n+1:
                continue
            if cur_index == n+1:
                saved_node = tru_head
            else:
                saved_node = saved_node.next
        if saved_node != None:
            saved_node.next = saved_node.next.next
        else:
            tru_head = tru_head.next
        return tru_head