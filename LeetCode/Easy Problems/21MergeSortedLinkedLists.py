# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Literally just a while loop maintaining that one of the lists hasnt ended yet
        # If one of the lists has ended, we can check to handle it in the while loop

        head = ListNode()
        iterator = head

        # Check if they're both negative

        while list1 or list2:
            if not list1:
                # When list1 is None
                iterator.next = list2
                list2 = list2.next
                
            elif not list2:
                # When list2 is None:
                iterator.next = list1
                list1 = list1.next
            else:
                # When we have both
                if list2.val < list1.val:
                    # We wanna insert the list2
                    iterator.next = list2
                    list2 = list2.next
                else:
                    # In any other case we're inserting list1
                    iterator.next = list1
                    list1 = list1.next
            iterator = iterator.next
        
        return head.next
                    
