class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = 0
        numlen = len(nums)
        k = 0
        for i in range(numlen):
        	if nums[k] == 0:
        		del nums[k]
        		t += 1
        	else:
        		k += 1
       	zeros = []
       	for i in range(t):
       		zeros.append(0)
        return nums.extend(zeros)
