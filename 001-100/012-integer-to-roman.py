class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  
        str_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  
        roman = ''  
        for i in range(len(num_list)):  
            while num >= num_list[i]:  
                num -= num_list[i]  
                roman += str_list[i]  
        return roman  
