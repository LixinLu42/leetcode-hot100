class Solution:
    def searchRange(self, nums, target):
        end = len(nums)
        start = 0
        return self.func(nums, target, start, end)

    def func(self, nums, target, start, end):
        if((end - start) <= 1 ):
            if(nums[start] == target):
                return [start, start]
            elif(nums[end] == target):
                return [end, end]
            else:
                return [-1, -1]

        if(nums[start] == target):
            while(nums[start] == target):
                tar_start = start
                start += 1
            tar_end = start - 1
            return [tar_start, tar_end]


        mid = start + (end - start)//2
        if(nums[mid] > target):
            return self.func(nums, target, start, mid)
        else:
            return self.func(nums, target, mid, end)

nums = [5, 10]
target = 8
a = Solution()
a.searchRange(nums, target)


        
