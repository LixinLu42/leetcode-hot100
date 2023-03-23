class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        n = len(s)
        k = -1
        ans = 0
        for i in range(n):
            if i != 0:
                seen.remove(s[i-1])
            while k+1 < n and  s[k+1] not in seen:
                seen.add(s[k+1])
                k+=1
            ans = max(ans, k-i+1)
        return ans
            
s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))
