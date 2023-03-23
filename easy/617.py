# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root1, root2)

    def dfs(self, root1, root2):
        if not (root1 and root2):
            return root1 if root1 else root2

        root1.val = root1.val + root2.val
        root1.left = self.dfs(root1.left, root2.left)
        root1.right = self.dfs(root1.right, root2.right)    
        return root1