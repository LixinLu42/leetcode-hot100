class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            # 异或运算满足交换律，a^b^a=a^a^b=b.
            res ^= num
        
        return res
         


num = [4,1,2,1,2]
a = Solution()
b = a.singleNumber(num)
print(b)