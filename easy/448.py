#  给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            x = (nums[i-1] - 1) % n
            nums[x] += n

        for j in range(n):
            if nums[j-1] <= n:
                res.append(j)

        return res
    
nums = [4,3,2,7,8,2,3,1]
a = Solution()

res  = a.findDisappearedNumbers(nums)
print(res)