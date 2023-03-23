# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 1.复制到数组
        # vec = []
        # while head:
        #     vec.append(head.val)
        #     head = head.next

        # return vec[:] == vec[::-1]

        # 2.递归
        # cur = head
        # if cur != None:
        #     if not self.isPalindrome(cur.next):
        #         return False
        #     if head.val != cur.val:
        #         return False
        #     head = head.next
        # return True
        # 3.双指针
        if not head:
            return True

        first_end = self.findmid(head)
        second_start =  self.fanzhuan(first_end.next)
        
        res = True
        while res and second_start != None:
            if first_end.val != second_start:
                return False  
        return True

    
        def findmid(head):
            slow = head
            fast = head
            while fast.next != None and fast.next.next != None:
                fast = head.next.next
                slow = head.next
            return slow


        def fanzhuan(head):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next          
            return pre
