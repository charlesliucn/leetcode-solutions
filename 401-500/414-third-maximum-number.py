class Solution(object):
	def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = list(set(nums))
		if len(nums) < 3:
			return max(nums)
		else:
			firstMax = max(nums)
			nums.remove(firstMax)
			secondMax = max(nums)
			nums.remove(secondMax)
			return max(nums)