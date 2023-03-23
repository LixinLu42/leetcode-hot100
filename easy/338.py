# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bits = [0]
        highbits = 0
        for i in range(1, n+1):
            if i&(i-1) == 0:
                highbits = i
            bits.append(bits[i - highbits] + 1)
        return bits

            
            

