class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        # result={} #存結果 次數pattern當key value 是一個list 裡面存所有anagrams字串
        result=defaultdict(list) #defaultdict會在 result[tuple(count)].append(s) 執行時 如果發現list是空的 自動建立一個空的list
    

        for s in strs:
            count=[0]*26 #
            for c in s: #一個字串中的一個字母
                count[ord(c) - ord('a')] +=1 #字母 出現次數+1
            result[tuple(count)].append(s)  #count是value list 不可以當dictionary 的key

        return list(result.values())
