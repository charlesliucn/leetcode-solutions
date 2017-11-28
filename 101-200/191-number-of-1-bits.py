class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = []
        while True:
        	if n == 0:
        		break
        	n, rem = divmod(n, 2)
        	bits.append(rem)
        return sum(bits)

# if __name__ == '__main__':
# 	t = Solution()
# 	print(t.hammingWeight(1451121451452145215211))