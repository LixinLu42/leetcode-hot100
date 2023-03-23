class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 1.动态规划
        # n = len(s)
        # if n < 2:
        #     return s

        # maxLen = 1
        # start = 0

        # #dp= [[False]*n]*n
        # dp = [[False] * n for _ in range(n)]
        # for k in range(n):
        #     dp[k][k] = True

        # for L in range(2, n+1):
        #     for i in range(n):
        #         R = L + i - 1

        #         if R >=n :
        #             break

        #         if s[i] != s[R]:
        #             dp[i][R] == False

        #         else:
        #             if R - i < 3:
        #                 dp[i][R] = True
        #             else:
        #                 dp[i][R] = dp[i+1][R-1]

        #         if dp[i][R] == True and maxLen < R-i+1:
        #             maxLen = R-i+1
        #             start = i 

        # return s[start : start+maxLen]


    #2.中心扩展法
        start,end = 0, 0
        for i in range(len(s)):
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i+1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l1 > end - start:
                start, end = l2, r2
        return s[start: end+1]

    def expand(self, s, l , r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return l+1, r-1



s = "abcabcbb"
a = Solution()
print(a.longestPalindrome(s))