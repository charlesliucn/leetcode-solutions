class Solution(object):
	def ipToCIDR(self, ip, ran):
		"""
		:type ip: str
		:type range: int
		:rtype: List[str]
		"""
		iplist = ip.split('.')
		ipbin = []
		for i in iplist:
			ipbin.extend(self.dec2bin(i))
		res = []
		for i in range(ran):
			tmp = ipbin[::-1].index(0)
			ipbin = self.addBinary(ipbin,[1])
			res.append(ip + "/" + str(32-tmp))
		print(res)

	def dec2bin(self, string_num):
		num = int(string_num)
		mid = []
		while True:
			if num == 0: break
			num,rem = divmod(num, 2)
			mid.append(rem)
		if len(mid) < 8:
			mid.extend([0]*(8-len(mid)))
		return mid[::-1]

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
		return res

if __name__ == '__main__':
	Solution().ipToCIDR("255.0.0.7",10)