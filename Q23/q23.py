from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        truhead = tail = None
        while not all(i == None for i in lists):
            min_val = float("inf")
            min_indexes = []
            for i, lst in enumerate(lists):
                if lst != None:
                    if lst.val < min_val:
                        min_val = lst.val
                        min_indexes = [i]
                    elif lst.val == min_val:
                        min_indexes.append(i)
            for i in min_indexes:
                if tail == None:
                    truhead = tail = lists[i]
                    lists[i] = lists[i].next
                else:
                    tail.next = lists[i]
                    tail = tail.next
                    lists[i] = lists[i].next
            
        return truhead

a = ListNode(5)
b = ListNode(4, a)
c = ListNode(1, b)

d = ListNode(4)
e = ListNode(3, d)
f = ListNode(1, e)

g = ListNode(6)
h = ListNode(2,g)

arr = [c, f, h]

x = Solution()
print( x.mergeKLists(arr) )