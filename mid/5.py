class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = 0
        dp = [][]

        for i in len(s):
            for j in range(i, len(s)):
                if dp[i][j] == True and s[i-1] == s[i+1]:
                    dp[]





s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))