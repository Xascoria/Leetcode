# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = out_head = None
        while not(list1 == None and list2 == None):
            if list1 == None:
                if output == None: return list2
                output.next = list2
                break
            elif list2 == None:
                if output == None: return list1
                output.next = list1
                break
            
            if (list1.val <= list2.val):
                if output == None:
                    out_head = output = list1
                else:
                    output.next = list1
                    output = output.next
                list1 = list1.next             
                output.next = None
            else:
                if output == None:
                    out_head = output = list2
                else:
                    output.next = list2
                    output = output.next
                list2 = list2.next             
                output.next = None   
        return out_head
                    
                    
                
            
        