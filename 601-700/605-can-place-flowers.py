import itertools
class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):
		"""
		:type flowerbed: List[int]
		:type n: int
		:rtype: bool
		"""
		num_times = [(k, len(list(v))) for k, v in itertools.groupby(flowerbed)]
		num_pieces = len(num_times)
		nexp = 0
		if num_pieces == 1:
			if num_times[0][0] == 0:
				nexp += (num_times[0][1]-1)//2 + 1
		else:
			if num_times[0][0] == 0:
				nexp += num_times[0][1]//2
			if num_times[num_pieces-1][0] == 0:
				nexp += num_times[num_pieces-1][1]//2
			for i in range(1, num_pieces-1):
				if num_times[i][0] == 0:
					nexp += (num_times[i][1]-1)//2
		if nexp >= n:
			return True
		else:
			return False
