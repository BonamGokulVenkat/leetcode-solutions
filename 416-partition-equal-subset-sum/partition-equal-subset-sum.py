class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        dp={}
        target=0
        for n in nums:
            target+=n
        if target % 2 != 0:
            return False
        target//=2

        def dfs(index,nums,target,dp):
            if target==0:
                return True
            if index<0: 
                return False
            key=(index, target)
            if key in dp:
                return dp[key]
            nottake=dfs(index-1,nums,target,dp)
            take=False
            if nums[index]<=target:
                take=dfs(index-1,nums,target-nums[index],dp)
            dp[key]=nottake or take
            return dp[key]
        return dfs(len(nums)-1,nums,target,dp)