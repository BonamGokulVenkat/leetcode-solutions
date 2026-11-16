class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (total + target) % 2:
            return 0
        
        dp={}

        def dfs(index,nums,target,dp):
            if index==len(nums):
                if target==0:
                    return 1
                else:
                    return 0
            key=(index,target)
            if key in dp:
                return dp[key]
            take=dfs(index+1,nums,target+nums[index],dp)
            nottake=dfs(index+1,nums,target-nums[index],dp)
            dp[key]=take+nottake
            return dp[key]
        return dfs(0,nums,target,dp)