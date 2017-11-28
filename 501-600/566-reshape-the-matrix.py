class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        merge = []
        numlen = len(nums)
        for s in nums:
        	merge.extend(s)
        num_all = len(merge)
        result = []
        if r*c != num_all:
        	return nums
        else:
        	tmp = []
        	for i in range(1, num_all+1):
        		if i % c != 0:
        			tmp.append(merge[i-1])
        		else:
        			tmp.append(merge[i-1])
        			result.append(tmp)
        			tmp = []
        return result


if __name__ == '__main__':
	t = Solution()
	m = [[1,2],[3,4]]
	print(t.matrixReshape(m,4,1))