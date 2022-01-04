# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        truheadA = headA
        while headA != None:
            headA.val = -headA.val
            headA = headA.next
        while headB != None:
            if headB.val < 0:
                output = headB
                while truheadA != None:
                    truheadA.val = -truheadA.val
                    truheadA = truheadA.next
                return output
            headB = headB.next
        while truheadA != None:
            truheadA.val = -truheadA.val
            truheadA = truheadA.next
        return None