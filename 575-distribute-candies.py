class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        num = len(candies)
        candies_unique = list(set(candies)) 
        num_unique = len(candies_unique)
        if  num_unique > num/2:
        	return int(num/2)
        else:
        	return int(num_unique)