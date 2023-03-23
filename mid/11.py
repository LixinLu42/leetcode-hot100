class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        r = n-1
        l = 0
        res = 0
        while l < r:
            area = (r-l)*min(height[l], height[r])
            res = max(res, area)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return res
height = [1,8,6,2,5,4,8,3,7]
a = Solution()
print(a.maxArea(height))