#k 代表前k名最常出現的數字
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count={}#只存key (數字的出現次數))

        # value 預設為 list ,key是nums大小+1
        #[[],[],[],[],[],[]]
        #是一個bucket list
        freq = [[]  for i in range(len(nums)+1)]  

        #計算數字的出現次數 {數字:出現次數}
        for num in nums:
            # count[num] : 用key取得values, 也就是取每個數字的出現次數 如果找不到key救回傳0
            count[num] = 1+count.get(num,0)        
        
        print(count)
        print(freq)
        #把出現次數存成key 數字存成value
        
        for num,f in count.items():
            freq[f].append(num)
        print(freq)
        
        res=[]
        for i in range(len(freq)-1,0,-1): #從出縣最多次的開始掃
            for num in freq[i]:
                res.append(num)
                if len(res)==k:  
                    return res   

        
        