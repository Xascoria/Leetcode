from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 1
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        traverse_node = head
        while traverse_node != None:
            if index % 2 == 1:
                if odd_head == None:
                    odd_head = traverse_node
                    odd_tail = traverse_node
                else:
                    odd_tail.next = traverse_node
                    odd_tail = odd_tail.next
            else:
                if even_head == None:
                    even_head = traverse_node
                    even_tail = traverse_node
                else:
                    even_tail.next = traverse_node
                    even_tail = even_tail.next
            traverse_node = traverse_node.next
            index += 1
        if head == None:
            return head
        odd_tail.next = even_head
        if even_tail:
            even_tail.next = None
        return odd_head
