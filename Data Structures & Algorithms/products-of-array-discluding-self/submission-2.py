class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        postfix=1 #累計的
        prefix=1 #因為第一個數字沒有prefix 

        #計算prefix, 放入res
        for i in range(len(nums)):  #---->
            res[i]=prefix
            prefix=prefix*nums[i] #蕾乘的結果
  
        right=1
        #再放postfix <----
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*right
            right*=nums[i]

        return res
