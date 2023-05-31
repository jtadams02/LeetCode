
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        finalNode = ListNode()
        travelerNode = finalNode # Linked List Traverser
        list1 = l1
        list2 = l2

        # This problem is a not more simpler than I made it. Essentially, it just addition by each place
        # We'll have to create a carry variable
        carry = 0
        # To keep track of the overflow
        
        # After that, we just need to loop through the two linked lists like wo

        while list1 or list2 or carry:
            # Now we just need to grab the value of each node key, if there is no node then just set it to 0
            # We'll have the variable be based at 0
            value1 = 0
            if list1:
                # If list1 is valid, then we change our value1
                value1 = list1.val
            # Now we do the same for value2
            value2 = 0
            if list2:
                # If list2 is valid, then we change value2
                value2 = list2.val

            # Now we need to add these 2 numbers, WITH A CARRY
            total_val = value1 + value2 + carry

            # This value could be overflow, and either way we need to clear or set the carry
            carry = total_val // 10 # Need to use floor division

            # And just incase our total value is greater than 10, we need the single digits place
            total_val = total_val % 10 # This should not change the single digit value because its a modulus operation

            # Now we need to append this value to the linked list
            travelerNode.next = ListNode(total_val)
            # Then incrememnet the traveler node
            travelerNode = travelerNode.next

            # Now we need to increment the linked lists, or set them to NULL 
            if list1:
                list1 = list1.next
            else:
                list1 = None

            if list2:
                list2 = list2.next
            else:
                list2 = None
        # Wait what if the carry is still around after, like in case 3??
        # Solved: Make the loop run again if the carry is non-null
        return finalNode.next



        # Poor Solution below
        
        # list1 = l1
        # newList1 = []
        # list2 = l2
        # newList2 = []

        # list3 = ListNode()

        # while list1 is not None:
        #     newList1.append(list1.val)
        #     list1=list1.next
        
        # while list2 is not None:
        #     newList2.append(list2.val)
        #     list2=list2.next
        
        # link1 = ""
        # while newList1:
        #     link1+=str(newList1.pop())
        
        # link2 = ""
        # while newList2:
        #     link2+=str(newList2.pop())
        

        # final = str(int(link1)+int(link2))
        # finalNode = ListNode()
        # tempNode = finalNode
        # first = 0
        # for c in reversed(final):
        #     if first==0:
        #         tempNode.val = int(c)
        #         first+=1
        #     else:
        #         newNode = ListNode()
        #         newNode.val = int(c)
        #         tempNode.next = newNode
        #         tempNode = tempNode.next
        
        # listFinal = finalNode
        # while listFinal is not None:
        #     print(listFinal.val)
        #     listFinal = listFinal.next

        # return finalNode
            
                





        

            