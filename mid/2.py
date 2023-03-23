class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return self.dfs(l1, l2)

    def dfs(self, l1, l2):
        if not (l1 and l2):
            return l1 if l1 else l2
        l1.val += l2.val    # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:
            l1.next = self.dfs(ListNode(l1.val // 10), l1.next)
            l1.val %= 10
        
        l1.next = self.dfs(l1.next, l2.next)
        return l1

    # 搞不懂为什么下边这个不行，和上边没区别
    # def dfs(self, l1, l2):
    #     if not (l1 and l2):
    #         return l1 if l1 else l2
    #     he = l1.val + l2.val        

    #     if he >= 10:
    #         l1.next = self.dfs(ListNode(he//10) , l1.next)
    #         l1.val = he % 10
        
    #     l1.next = self.dfs(l1.next, l2.next)
    #     return l1
