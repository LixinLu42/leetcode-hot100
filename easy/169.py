class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums)//2)]

nums = [2,2,1,1,1,2,2]
a = Solution()

res  = a.majorityElement(nums)
print(res)

        