class Solution(object):
	def pivotIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sumall = sum(nums)
		if len(nums) > 0 and sumall - nums[0] == 0:
			return 0
		sumtmp = 0
		if len(nums) == 1:
			return 0
		for i in range(1,len(nums)):
			half = (sumall - nums[i])/2.0
			sumtmp += nums[i-1]
			if sumtmp == half:
				return i
		return -1