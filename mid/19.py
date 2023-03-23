# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1.双指针
        # l1 = head

        # head2 = ListNode(0, head)
        # l2 = head2

        # for i in range(n):
        #     l1 = l1.next

        # while l1:
        #     l1 = l1.next
        #     l2 = l2.next
        # l2.next = l2.next.next
        # return head2.next

        # 2.栈
        head1 = ListNode(0, head)
        stack = list()
        cur = head1
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()

        pre = stack[-1]
        pre.next = pre.next.next
        return head1.next