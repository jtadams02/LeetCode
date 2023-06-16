# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # This is pretty simple, all we need to do is have a current and a previous variable
        # We can just loop through the linked list and have each curr point to the prevous node
        # Will need a temp variable 

        curr = head
        prev = curr

        while curr:
            temp = curr.next
            # If we're at the first iteration, we need to make sure that the head points to None
            if curr == prev:
                # Beginning case
                curr.next = None
            else:
                # Otherwise, we just make curr point to the previous node
                curr.next = prev
            
            # Set the previous node to curr
            prev = curr
            # And change curr to the node it used to point too
            curr = temp
        # We set prev to the head because our loop makes curr = None
        head = prev
        return head