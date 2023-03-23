# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return root

            l = dfs(root.left)
            r = dfs(root.right)

            root.left = r
            root.right = l
            return root

        return dfs(root)

