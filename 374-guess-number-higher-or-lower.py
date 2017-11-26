# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		first = 1
		second = n
		if guess(n) == 0:
			return n
		while True:
			guessnum = int((first+second)/2)
			if guess(guessnum) == 0:
				return guessnum
			elif guess(guessnum) == -1:
				second = guessnum
			else:
				first = guessnum