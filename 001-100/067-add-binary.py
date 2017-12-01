class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		if a == "":
			return b
		if b == "":
			return a
		a = [int(c) for c in a]
		b = [int(c) for c in b]
		a.reverse()
		b.reverse()
		lena = len(a)
		lenb = len(b)
		if lena < lenb:
			a.extend([0]*(lenb - lena))
		else:
			b.extend([0]*(lena - lenb))
		carry = 0
		res = []
		print(a)
		print(b)
		for i in range(max(lena, lenb)):
			tmp = a[i] + b[i] + carry
			if tmp == 2:
				tmp = 0
				carry = 1
			else:
				carry = 0
			res.append(tmp)
		if carry == 1:
			res.append(carry)
		res.reverse()
		res = [str(i) for i in res]
		res = "".join(res)
		return res

if __name__ == '__main__':
	print(Solution().addBinary("0","0"))