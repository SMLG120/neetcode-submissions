# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
            



        # # reverse l1
        # prev1 = None
        # while l1 and l1.next:
        #     tmp1 = l1.next
        #     l1.next = prev1
        #     prev1 = l1
        #     l1 = tmp1
        
        # # reverse l2
        # prev2 = None
        # while l2 and l2.next:
        #     tmp2 = l2.next
        #     l2.next = prev2
        #     prev2 = l2
        #     l2 = tmp2

        # # compute sum
        # sum = 0
        # while l1 and l1.next and l2 and l2.next:
        #     minisum = l1.val + l2.val
        #     sum += minisum
        #     sum *= 10
        #     l1 = l1.next
        #     l2 = l2.next

        # # reverse sum back

    