# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None

        length = 0
        tranverse_node = head
        while tranverse_node != None:
            length += 1
            tranverse_node = tranverse_node.next
        half = length//2

        tranverse_node = head
        cur_index = 0
        while tranverse_node != None:
            if cur_index == half-1:
                tranverse_node.next = tranverse_node.next.next
            cur_index += 1
            tranverse_node = tranverse_node.next
        return head