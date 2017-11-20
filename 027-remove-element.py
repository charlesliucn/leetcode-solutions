class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		try:
			for i in range(len(nums)):
				nums.remove(val)
		except ValueError:
			return nums