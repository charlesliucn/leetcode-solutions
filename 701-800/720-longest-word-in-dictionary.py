class Solution:
	def longestWord(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""
		words.sort()
		words = sorted(words,key = lambda x: len(x), reverse = True)

		for w in words:
			flag = 0
			if len(w) == 1:
				return w
			tmp = w[:-1]
			for c in range(len(w)-1):
				if tmp in words:
					if len(tmp) == 1:
						flag = 1
					tmp = tmp[:-1]
				else:
					break
			if flag == 1:
				return w
		return ""

# if __name__ == '__main__':
# 	t = Solution()
# 	print(t.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))