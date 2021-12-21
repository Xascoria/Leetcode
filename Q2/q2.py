# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while l1 != None:
            a.append(l1.val)
            l1 = l1.next
        b = []
        while l2 != None:
            b.append(l2.val)
            l2 = l2.next
        c = max(len(a),len(b))
        a = a + (len(a)-c)*[0]
        b = b + (len(b)-c)*[0]
        a = int("".join(map(str,a))[::-1])
        b = int("".join(map(str,b))[::-1])
        #print(a+b)
        output = [*map(int,str(a+b))]
        end = ListNode(output[0])
        for i in output[1:]:
            end = ListNode(i,end)
        return end
        