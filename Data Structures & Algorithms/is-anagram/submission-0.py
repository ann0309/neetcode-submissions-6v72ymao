# from collections import Counter #計算兩個dictionary 是否出現次數依樣

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}

        for i in s:
            if i in dict_s:
                dict_s[i]=dict_s.get(i)+1
            else:
              dict_s[i]=1  
        for i in t:
            if i in dict_t:
                dict_t[i]=dict_t.get(i)+1
            else:
              dict_t[i]=1  
        
        return dict_s==dict_t