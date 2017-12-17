class Solution(object):
	def areSentencesSimilar(self, words1, words2, pairs):
		"""
		:type words1: List[str]
		:type words2: List[str]
		:type pairs: List[List[str]]
		:rtype: bool
		"""
		count = 0
		wordslen1 = len(words1)
		wordslen = len(words2)
		if wordslen1 != wordslen:
			return False
		for i in range(wordslen):
			if words1[i] == words2[i]:
				count += 1
			else:
				group = [words1[i],words2[i]]
				if group in pairs or group[::-1] in pairs:
					count += 1
		if count == wordslen:
			return True
		else:
			return False

if __name__ == '__main__':
	t = Solution()
	print(t.areSentencesSimilar(["great","acting","skills","skills"],["fine","drama","talent"],[["great","fine"],["drama","acting"],["skills","talent"]]))