class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[i-1] and i > 0:
                continue
            target = -1 * nums[i]
            l, r = i+1, n-1
            
            while l < r:
                if (r<n-1 and nums[r] == nums[r+1]):
                    r-=1
                    continue
                if l > i+1 and nums[l] == nums[l-1]:
                    l+=1
                    continue
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res

        