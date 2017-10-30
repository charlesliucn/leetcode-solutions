class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        len2 = len(nums2)
        r = []
        for i in nums1:
        	index = nums2.index(i)
        	flag = 0
        	for j in range(index,len2):
        		if nums2[j] > i:
        			t = nums2[j]
        			flag = 1
        			break
        	if flag == 0:
        		t = -1
        	r.append(t)
        return r
    
