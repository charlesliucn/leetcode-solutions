class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
    	num = map(int, str(n))
    	sumsquare = 0
    	history = [0]
    	while True:
    		numsquare = [i*i for i in num]
    		sumsquare = sum(numsquare)
    		if sumsquare == 1:
    			return True
    		if sumsquare not in history:
    			history.append(sumsquare)
    			num = map(int, str(sumsquare))
    		else:
    			return False