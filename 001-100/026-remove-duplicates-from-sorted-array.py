class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		i = 1
		numslen = len(nums)
		while i < numslen:
			if nums[i] == nums[i-1]:
				del nums[i]
				numslen -= 1
			else:
				i += 1
		return numslen