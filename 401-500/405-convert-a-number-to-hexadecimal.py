class Solution(object):
	def toHex(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num == 0:
			return "0"
		elif num > 0:
			return self.dec2hexpos(num)
		else:
			num = 4294967296 + num
			return self.dec2hexpos(num)

	def dec2hexpos(self, num):
		mid = ""
		while True:
			if num == 0: 
				break
			num, rem = divmod(num, 16)
			if rem == 10:
				mid = "a" + mid
			elif rem == 11:
				mid = "b" + mid
			elif rem == 12:
				mid = "c" + mid
			elif rem == 13:
				mid = "d" + mid
			elif rem == 14:
				mid = "e" + mid
			elif rem == 15:
				mid = "f" + mid
			else:
				mid = str(rem) + mid
		return mid