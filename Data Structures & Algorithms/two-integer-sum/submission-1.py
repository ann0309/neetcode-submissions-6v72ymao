class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1,index2=0,1
        print("index1",index1,"index2",index2)
        while index1<len(nums) and index2<len(nums):
            tmp=target-nums[index1]
            print("是否找到?:",nums[index2]==tmp)
            if nums[index2]==tmp:
                return [index1,index2]
            else: 
                index2+=1
                
            if index2==len(nums):
                index1+=1
                index2=index1+1
            print("index1",index1,"index2",index2)