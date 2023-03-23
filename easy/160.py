class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seena = set()
        while headA:
            seena.add(headA)
            headA = headA.next

        while headB:
            if headB in seena:
                return headB

            headB = headB.next 
        return headB
            



