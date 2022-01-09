from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return None

        traverse_node = head
        list_length = 0
        while traverse_node != None:
            list_length += 1
            traverse_node = traverse_node.next
        shift = (list_length - k) % list_length
        if shift == 0: return head
        traverse_node = head
        prev_node = None
        while shift != 0:
            prev_node = traverse_node
            traverse_node = traverse_node.next
            shift -= 1
        new_output = traverse_node
        prev_node.next = None
        while traverse_node.next != None:
            traverse_node = traverse_node.next
        traverse_node.next = head
        return new_output

        