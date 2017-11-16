class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices != []:
        	small = prices[0]
        	for i in prices[1:]:
        		small = min(i, small)
        		profit = max(i - small, profit)
        return profit