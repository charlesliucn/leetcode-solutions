class Solution(object):
	def findMaxAverage(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: float
		"""
		numslen = len(nums)
		if numslen <= k:
			return (sum(nums)+0.0)/k
		else:
			maximum = sum(nums[0:k])
			tmpsum = maximum
			i = k
			while i < numslen:
				tmp = tmpsum - nums[i-k] + nums[i]
				if tmp > maximum:
					maximum = tmp
				i += 1
		return (maximum+0.0)/k

if __name__ == '__main__':
	t = Solution()
	print(t.findMaxAverage([3,3,4,3,0],3))