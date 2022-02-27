from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head

        def recursion(head, length):
            if length == 1:
                head.next = None
                return head

            if length % 2:
                tranverse_node = left_head = head
                for i in range(length//2):
                    tranverse_node = tranverse_node.next
                right_head = tranverse_node
                left_length = length//2
                right_length = length - left_length
            else:
                left_head = tranverse_node = head
                for i in range(length//2):
                    tranverse_node = tranverse_node.next
                right_head = tranverse_node
                left_length = right_length = length//2

            a = recursion(left_head, left_length)
            b = recursion(right_head, right_length)
            new_head = None
            new_tail = None
            while a != None and b != None:
                if a.val > b.val:
                    if new_head == None:
                        new_head = b
                        new_tail = b
                    else:
                        new_tail.next = b
                        new_tail = new_tail.next
                    b = b.next
                else:
                    if new_head == None:
                        new_head = a
                        new_tail = a
                    else:
                        new_tail.next = a
                        new_tail = new_tail.next
                    a = a.next
            if a != None:
                new_tail.next = a
            else:
                new_tail.next = b
            return new_head

        tranverse_node = head
        length = 0
        while tranverse_node != None:
            length += 1
            tranverse_node = tranverse_node.next
        return recursion( head, length )

                


            

            