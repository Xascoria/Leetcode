from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        truhead = None
        prev_node = None
        tranverse_node = head
        while tranverse_node != None:
            if tranverse_node.val != val:
                if truhead == None:
                    truhead = tranverse_node
                    prev_node = tranverse_node
                else:
                    prev_node.next = tranverse_node
                    prev_node = prev_node.next
            tranverse_node = tranverse_node.next
        if prev_node != None: prev_node.next = None
        return truhead
