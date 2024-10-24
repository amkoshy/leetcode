# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.
class Solution(object):
    def lengthOfLastWord(self, s):
        blah= s.split()
        if len(blah)<1:
            return 0
        else:
            return len(s.split()[-1])
        """
        :type s: str
        :rtype: int
        """
