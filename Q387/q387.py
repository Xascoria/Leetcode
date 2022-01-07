# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randrange

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        current_index = 2
        current_val = self.head.val
        current_node = self.head.next
        while current_node != None:
            if randrange(current_index) == 1:
                current_val = current_node.val
                
            current_node = current_node.next
            current_index += 1
        return current_val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()