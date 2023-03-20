class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """     
        minprices = 1000000
        maxprofit = 0
        for price in prices:
            minprices = min(minprices, price)
            maxprofit = max(maxprofit, price - minprices)
        return maxprofit

price = [7,1,5,3,6,4]
#price = [7,6,4,3,1]
a = Solution()
b = a.maxProfit(price)
print(b)