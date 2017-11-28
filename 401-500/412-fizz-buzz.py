class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        for i in range(n):
        	if i % 3 == 0 and i % 5 != 0:
        		r.append("Fizz")
        	elif i % 5 == 0 and i % 3 != 0:
        		r.append("Buzz")
        	elif i % 5 == 0 and i % 3 == 0:
        		r.append("FizzBuzz")
        	else r.append(str(i))
        return r