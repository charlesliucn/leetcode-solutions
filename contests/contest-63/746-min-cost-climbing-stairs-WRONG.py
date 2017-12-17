class Solution(object):
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		totalcost0 = self.minCostTest(cost)
		cost = cost[1:]
		totalcost1 = self.minCostTest(cost)
		return min(totalcost0, totalcost1)

	def minCostTest(self, cost):
		costlen = len(cost)
		i = 0
		totalcost = cost[0]
		if costlen <= 2:
			return totalcost
		while i < costlen - 1:
			if i == costlen - 2:
				break
			if cost[i+1] < cost[i+2]:
				totalcost += cost[i+1]
				i += 1
			else:
				totalcost += cost[i+2]
				i += 2
		return totalcost

if __name__ == '__main__':
	print(Solution().minCostClimbingStairs( [0,1,1,0]))