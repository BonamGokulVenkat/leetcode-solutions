class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1]*(len(nums))
        return self.helper(len(nums)-1,nums,dp)
    def helper(self,ind,nums,dp):
        if ind==0:
            return nums[ind]
        if ind==-1:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        pick=nums[ind]+self.helper(ind-2,nums,dp)
        notPick=self.helper(ind-1,nums,dp)
        dp[ind]=max(pick,notPick)
        return dp[ind]