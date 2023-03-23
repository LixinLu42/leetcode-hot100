class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):           
        if not (left or right):
            return True

        if not (left and right):
            return False

        if left.val != right.val:
            return False

        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
