# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # 1
        # head = ListNode(-1)
        # pre = head

        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         pre.next = l1
        #         l1 = l1.next
        #     else:
        #         pre.next = l2
        #         l2 = l2.next
        #     pre = pre.next
        # pre.next = l1 if l1 is not None else l2
        # return head.next

        #2
        if l1 is not None:
            return l1
        elif l2 is not None:
            return l2
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        


            
            
