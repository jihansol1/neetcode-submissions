# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        sumList = dummy

        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            val = x + y + carry
            # carrying either 0 or 1 depending on val > 10 or not
            carry = val // 10
            # new digit appended as a result of addition
            digit = val % 10
            sumList.next = ListNode(digit)
            sumList = sumList.next

            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        