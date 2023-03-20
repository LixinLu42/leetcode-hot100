# 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        res = list()

        for a in range(l):
            if nums[a] >0:
                continue

            if a > 0 and nums[a] == nums[a-1]:
                continue 
            target = -nums[a]
            c = l-1

            for b in range(a+1, l):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                while b < c and (nums[b] + nums[c]) > target:
                    c-=1
                if b == c:
                    break

                if nums[b] + nums[c] == target:
                    res.append([nums[a], nums[b], nums[c]])
        return res
nums = [-1,0,1,2,-1,-4]
a = Solution()
print(a.threeSum(nums))
