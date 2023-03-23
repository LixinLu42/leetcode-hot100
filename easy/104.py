# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        du = 1
        return self.dfs(root.left, root.right, du)


    def dfs(self, left, right, du):
        if not (left or right):
            return du
        du += 1
        if not (left and right):
            du += 1
            if not left:
                return self.dfs(right.left, right.right, du)
            elif not right:
                return self.dfs(left.left, left.right, du)
        return max(self.dfs(left.left, left.right, du),  self.dfs(right.left, right.right, du))

        
