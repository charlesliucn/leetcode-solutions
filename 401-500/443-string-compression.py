class Solution(object):
	def compress(self, chars):
		"""
		:type chars: List[str]
		:rtype: int
		"""
		charslen = len(chars)
		i = 0
		count = 1
		while i < charslen:
			while i < charslen - 1:
				if chars[i+1] == chars[i]:
					popup = chars.pop(i+1)
					charslen -= 1
					count += 1
				else:
					break
			if count == 1:
				i += 1
			else:
				tmp = list(str(count))
				for c in tmp:
					i += 1
					chars.insert(i,c)
					charslen += 1
				i += 1
			count = 1
		return len(chars)