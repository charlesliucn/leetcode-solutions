from collections import Counter
class Solution(object):
	def findPairs(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		res = 0
		if k == 0:
			dic = Counter(nums)
			dic_tmp = [d for d in dic.values() if d > 1]
			res = len(dic_tmp)
			return res
		elif k > 0:
			nums = set(nums)
			nums_tmp = set([n+k for n in nums])
			res = len(nums & nums_tmp)
			return res
		else:
			return 0
