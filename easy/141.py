class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        ###解法1：集合
        # seen = set()

        # while head:
        #     if head in seen:
        #         return True 
        #     seen.add(head)
        #     head = head.next
        # return False


        ####解法2：快慢指针
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


class ListNode:
    def __init__(self, x) -> None:
        self.val = x 
        self.next = None

class LinkList:
    def __init__(self) -> None:
        self.head = None

    def initList(self, data):
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

data1 = [3, 2, 0, -4]
linklist = LinkList()
link = linklist.initList(data1)
a = Solution()
b = a.hasCycle(link)
print(b)
