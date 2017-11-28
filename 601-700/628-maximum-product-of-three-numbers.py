from copy import deepcopy
class Solution(object):
	def maximumProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		numsmaxs = heapq.nlargest(3, nums)
		numsmins = heapq.nsmallest(2, nums)
		res1 = numsmaxs[0]*numsmaxs[1]*numsmaxs[2]
		res2 = numsmins[0]*numsmins[1]
		return max(res1,res2)