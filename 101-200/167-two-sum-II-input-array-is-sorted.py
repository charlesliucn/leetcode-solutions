class Solution(object):
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		numlen = len(numbers)
		bottom = 0
		up = numlen - 1
		while numbers[bottom] + numbers[up] != target:
			if numbers[bottom] + numbers[up] < target:
				bottom += 1
			else:
				up -= 1
		return [bottom+1, up+1]
