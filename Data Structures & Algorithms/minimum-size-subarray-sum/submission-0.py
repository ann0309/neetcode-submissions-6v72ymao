class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total=0
        min_length=1000000
        if "" or sum(nums)<target:
            return 0
        
        if nums[0]>=target:
            return 1
        for i in range(0,len(nums)):
            start=i #index
            total=nums[i]
            
            # print("-------------------------Start=",i,"------------------------------------")
            for j in range(i+1,len(nums)):
                # print("Left=",j,"------------------------------------")
                right=j
                if nums[j]>=target:
                    return 1
                elif nums[j]+total>=target: #如果大於等於target
                    min_length=min(min_length,right-start+1)
                    # print("min_length=",min_length,"sum=",total)
                    total=0
                    break
                total+=nums[j]
                # print("sum=",total)
        return min_length

                