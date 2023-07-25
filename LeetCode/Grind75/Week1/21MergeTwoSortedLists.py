# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = list1
        n2 = list2
        head = ListNode()
        l = head
        while n1 or n2:
            if not n2:
                # When there is only n1
                l.next = n1
                n1 = n1.next
            elif not n1:
                # When there is only n2
                l.next = n2
                n2 = n2.next
            else:
                # When there is both
                if n2.val < n1.val:
                    # We put n2
                    l.next = n2
                    n2 = n2.next
                else:
                    # We place n1
                    l.next = n1
                    n1 = n1.next
            l = l.next

        return head.next


        