class Solution(object):
	def asteroidCollision(self, asteroids):
		"""
		:type asteroids: List[int]
		:rtype: List[int]
		"""
		import copy
		if len(asteroids)== 1:
			return asteroids
		lens = len(asteroids)
		oldaster = copy.deepcopy(asteroids)
		i = 0
		while i < lens-1:
			if self.sign(asteroids[i]) != self.sign(asteroids[i+1]):
				if abs(asteroids[i]) < abs(asteroids[i+1]):
					asteroids.pop(i)
					lens -= 1
				elif abs(asteroids[i]) > abs(asteroids[i+1]): 
					asteroids.pop(i+1)
					lens -= 1
				else:
					asteroids.pop(i)
					asteroids.pop(i)
					lens -= 2
			i += 1
			if lens == 1:
				return asteroids

		while oldaster != asteroids:
			i = 0
			oldaster = copy.deepcopy(asteroids)
			while i < lens-1:
				if lens== 1:
					return asteroids
				if self.sign(asteroids[i]) != self.sign(asteroids[i+1]):
					if abs(asteroids[i]) < abs(asteroids[i+1]):
						asteroids.pop(i)
						lens -= 1
					elif abs(asteroids[i]) > abs(asteroids[i+1]): 
						asteroids.pop(i+1)
						lens -= 1
					else:
						asteroids.pop(i)
						asteroids.pop(i)
						lens -= 2
				i += 1
				if len(asteroids) == 1:
					return asteroids
		return asteroids
	def sign(self,x):
		if x > 0:
			return 1
		elif x < 0:
			return -1