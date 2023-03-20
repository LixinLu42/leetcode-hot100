# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# #请注意 ，必须在不复制数组的情况下原地对数组进行操作
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in range(len(nums)):
            if 0 != nums[i]:
                tmp = nums[a]
                nums[a] = nums[i]
                nums[i] = tmp
                a += 1
        return nums
                
nums = [0,1,0,3,12]
a = Solution()
print(a.moveZeroes(nums))
