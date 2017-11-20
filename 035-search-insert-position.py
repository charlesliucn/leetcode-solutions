class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""

		numslen = len(nums)
		if target <= nums[0]:
			return 0
		if target > nums[numslen-1]:
			return numslen
		index = 0
		for i in range(numslen):
			if target > nums[i]:
				index += 1
			if target < nums[i]:
				return index
			if target == nums[i]:
				return index
