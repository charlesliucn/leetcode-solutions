class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1 or n == 0:
        # 	return 1
        # elif n == 2:
        # 	return 2
        # else:
        # 	return self.climbStairs(n-1)+self.climbStairs(n-2)
        first = 0
        second = 1
        fn = 0
        for i in range(2,n+1):
            fn = first + second
            first = second
            second = fn
        return fn