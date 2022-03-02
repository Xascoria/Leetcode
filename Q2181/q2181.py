# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head.next
        cur_val = 0
        
        return_head = None
        return_tail = None
        while start != None:
            if start.val != 0:
                cur_val += start.val
            else:
                if return_head == None:
                    return_head = return_tail = ListNode(cur_val)
                else:   
                    return_tail.next = ListNode(cur_val)
                    return_tail = return_tail.next
                cur_val = 0
            start = start.next
        return return_head