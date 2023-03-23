#两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = x^y
        num = 0
        while ret:
            ret &= (ret-1)
            num+=1
        return num

x = 10
y = 11
a = Solution()
print(a.hammingDistance(x, y))
