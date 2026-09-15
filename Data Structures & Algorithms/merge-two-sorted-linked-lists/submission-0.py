# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sorted_list = ListNode()
        new_head = sorted_list

        while list1 and list2:
            if list1.val > list2.val:
                new_head.next = list2
                list2 = list2.next
            else:
                new_head.next = list1
                list1 = list1.next
            new_head = new_head.next

        # if either list is terminated
        if not list1:
            new_head.next = list2
        else:
            new_head.next = list1

        return sorted_list.next
        