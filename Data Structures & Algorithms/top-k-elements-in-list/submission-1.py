#k 代表前k名最常出現的數字
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=defaultdict(int) #如果要加入的時候是空的 就幫忙設定型態
        output=[]

        for num in nums:
            result[num]+=1
        top2 = sorted(result.values(), reverse=True)[:k] #是value
        print(top2)

        for key,values in result.items():
            print("key:",key,"values:",values)
            if values in top2:
                output.append(key)

        return output