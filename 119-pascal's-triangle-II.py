class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex):
        	newrow = [1]*(i+1)
        	if i == 0 or i == 1:
        		res.append(newrow)
        	else:
        		lastrow = res[i-1]
        		for j in range(1, i):
        			newrow[j] = lastrow[j-1] + lastrow[j]
        		res.append(newrow)
        return res[rowIndex]