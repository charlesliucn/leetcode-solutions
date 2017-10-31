class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        NUM = 26
        flag = []
        for i in range(NUM):
        	flag.append(0)
        for i in list(s):
        	flag[ord(i) - ord('a')] += 1
        for i in list(t):
        	flag[ord(i) - ord('a')] -= 1
        	if flag[ord(i) - ord('a')] == -1:
        		return i

if __name__ == '__main__':
	t = Solution()
	print(t.findTheDifference("abcszcjsnjzd","szcjsnjzabcde"))