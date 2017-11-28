class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
        	return m*n
        first = [x[0] for x in ops]
        second = [x[1] for x in ops]
        return min(first)*min(second)

    	

if __name__ == '__main__':
	s = Solution()
	t = s.maxCount(3,4,[[2,2],[3,3],[3,4],[4,4],[1,4]])
	print(t)