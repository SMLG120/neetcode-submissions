# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        pointer2 = dummy
        pointer1 = head
        counter = 0
        while counter < n:
            pointer1 = pointer1.next
            counter += 1

        # At this stage of the code, pointer1 is nth away from pointer2

        while pointer1: # go till pointer1 reaches end, move both pointers
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        # now pointer is right before the node to delete (pointer2.next) so skip it.
        pointer2.next = pointer2.next.next

        return dummy.next
        



        
