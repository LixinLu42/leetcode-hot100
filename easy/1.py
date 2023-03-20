class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1.哈希表
        # l =len(nums)
        # hashtable = dict()
        # for i in range(l):
        #     if target - nums[i] in hashtable:
        #         return [hashtable[target-nums[i]], i]
        #     hashtable[nums[i]] = i
        # return []

        # 2.暴力
        l =len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

nums = [2,7,11,15]
target = 9
a = Solution()
print(a.twoSum(nums, target))
    