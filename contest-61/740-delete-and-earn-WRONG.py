from collections import Counter
class Solution(object):
	def deleteAndEarn(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		table = Counter(nums)
		points = 0
		while nums != []:
			maxi = max(nums)
			tmpvalue1 = table[maxi]*maxi
			if maxi-1 in nums:
				tmpvalue2 = table[maxi-1]*(maxi-1)
				if tmpvalue1 >= tmpvalue2:
					points += maxi
					nums.remove(maxi)
					while maxi-1 in nums:
						nums.remove(maxi-1)
				else:
					points += maxi-1
					nums.remove(maxi - 1)
					while maxi in nums:
						nums.remove(maxi)
					while maxi-2 in nums:
						nums.remove(maxi-2)
			else:
				points += tmpvalue1
				nums.remove(maxi)
		return points

if __name__ == '__main__':
	print(Solution().deleteAndEarn([8,6,1,7,5,8,9,5,1,1,7,3,5,8,5,2,9,6,9,10,10,10,4,4,8,8,4,3,6,7,4,5,1,7,1,5,1,6,7,9,6,4,8,7,9,7,8,2,9,5]))