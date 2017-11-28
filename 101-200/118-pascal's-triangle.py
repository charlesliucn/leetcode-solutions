class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
        	newrow = [1]*(i+1)
        	if i == 0 or i == 1:
        		res.append(newrow)
        	else:
        		lastrow = res[i-1]
        		for j in range(1, i):
        			newrow[j] = lastrow[j-1] + lastrow[j]
        		res.append(newrow)
        return res

# if __name__ == '__main__':
# 	t = Solution()
# 	print(t.generate(5))