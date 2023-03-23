class Solution(object):
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]

        def find(tempmaxSum, tmpSum):
            if tempmaxSum < tmpSum:
               tempmaxSum = tmpSum
            
            return tempmaxSum

        for i in range(0, len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]
                maxSum = find(maxSum, sum)
        
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
aa = Solution()

res  = aa.maxSubArray(nums)
print(res)
