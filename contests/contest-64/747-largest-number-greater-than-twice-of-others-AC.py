class Solution(object):
	def dominantIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		max1 = max(nums)
		index = nums.index(max1)
		nums.remove(max1)
		max2 = max(nums)
		if max1 >= 2*max2:
			return index
		else:
			return -1