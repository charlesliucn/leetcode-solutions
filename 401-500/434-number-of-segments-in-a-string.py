class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        seglist = s.split(" ")
        seglist = [s for s in seglist if len(s) > 0]
        return len(seglist)
        print(seglist)
if __name__ == '__main__':
	t = Solution()
	print(t.countSegments("Hello World, ha aha          haha ha"))