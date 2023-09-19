class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_list = []
     
        max_length = 0
        for x in s:
            if x not in current_list:                 
                current_list.append(x)
                if max_length < len(current_list):
                    max_length = len(current_list)
            else:
                current_list.append(x)               
                current_list = current_list[current_list.index(x)+1:]           
        return max_length