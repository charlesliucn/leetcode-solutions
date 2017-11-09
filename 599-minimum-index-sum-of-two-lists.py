class Solution(object):
	def findRestaurant(self, list1, list2):
		"""
		:type list1: List[str]
		:type list2: List[str]
		:rtype: List[str]
		"""
		minfind = []
		numlist1 = len(list1)
		numlist2 = len(list2)
		minindex = numlist1 + numlist2

		for i in range(numlist1):
			if list1[i] in list2:
				tmpindex = i + list2.index(list1[i])
				if tmpindex < minindex:
					minindex = tmpindex
					minfind.append(list1[i])
				elif tmpindex == minindex:
					minfind.append(list1[i])
		return minfind

if __name__ == '__main__':
	t = Solution()
	s = t.findRestaurant(["Shogun", "KFC", "Tapioca Express", "Burger King"],["KFC", "Shogun", "Burger King"])
	print(s)