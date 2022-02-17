# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crit_encountered = False

        cur_node = head.next
        prev_dist = -1
        first_dist = -1
        prev_val = head.val
        current_index = 0
        output = [float('inf'),float('inf')]
        while cur_node.next != None:
            if (prev_val < cur_node.val and cur_node.val > cur_node.next.val) or \
                (prev_val > cur_node.val and cur_node.val < cur_node.next.val):
                if not crit_encountered:
                    first_dist = current_index
                    prev_dist = current_index
                    crit_encountered = True
                else:
                    output[0] = min(output[0], current_index-prev_dist)
                    output[1] = current_index - first_dist
                    prev_dist = current_index
            prev_val = cur_node.val
            cur_node = cur_node.next
            current_index += 1
        if output[0] == float('inf'):
            return [-1,-1]
        return output