class Solution:
    def romanToInt(self, s: str) -> int:
        list_s = list(s)

        two_s=["IV","IX","XL","XC","CD","CM"]
        two_values = [4,9,40,90,400,900]
        one_s=["I", "V", "X", "L", "C", "D", "M"]
        one_values = [1,5,10,50,100,500,1000]

        value =0
        for x in range(0,len(two_s)):    
            if s.find(two_s[x])>-1:
                value = value + two_values[x]              
                del list_s[s.find(two_s[x])+1]       
                del list_s[s.find(two_s[x])]

        for x in range(0,len(one_s)):   
            value = value + (one_values[x])*list_s.count(one_s[x])
        return value