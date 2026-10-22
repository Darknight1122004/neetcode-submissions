class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=float('inf') 
        if k==1:
            return 0  
        for i in range(len(nums) -k +1):
                  cur=nums[i+k-1]-nums[i]
                  res=min(res,cur) 
        return res       
        