import numpy as np

class Solution(object):
	def hammingDistance(self, x, y):
		xbin = self.dec2bin(x)
		ybin = self.dec2bin(y)
		xbin = np.array(xbin)
		ybin = np.array(ybin)
		len1 = len(xbin)
		len2 = len(ybin)
		if len1 > len2:
			ybin = np.append(np.zeros(len1-len2),ybin)
		elif len1 < len2:
			xbin = np.append(np.zeros(len2-len1),xbin)
		r = xbin - ybin
		rlist = [i for i in r if i != 0]
		return len(rlist)
    
	def dec2bin(self,num):
		binary = []
		while True:
			if num == 0: break
			num, re = divmod(num, 2)
			binary.insert(0,re)
		return binary