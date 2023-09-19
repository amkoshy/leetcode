class Solution(object):
    def isPalindrome(self, x):
        if x>=0 and str(x) == str(x)[::-1]:
            return True
        else:
            return False
           
        """
        :type x: int
        :rtype: bool
        """