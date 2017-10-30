class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        listzero = [i for i, a in enumerate(nums) if a == 0]
        listzero.insert(0,-1)
        listzero.append(numlen)
        indexlen = len(listzero)
        # print(listzero)
        MAXLEN = 0
        for i in range(1, indexlen):
        	temp = listzero[i] - listzero[i-1] -1
        	if temp > MAXLEN:
        		MAXLEN = temp
        return MAXLEN
# if __name__ == '__main__':
# 	t = Solution()
# 	s = t.findMaxConsecutiveOnes([1,1,0,1])
# 	print(s)