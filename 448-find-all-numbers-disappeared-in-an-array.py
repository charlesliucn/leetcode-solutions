class Solution:
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if nums == []:
			return []
		numlen = len(nums)
		boollist = []
		r = []
		for i in range(numlen):
			boollist.append(False)
		for i in nums:
		    boollist[i-1] = True
		for i in range(numlen):
			if boollist[i] == False:
				r.append(i+1)
		return r