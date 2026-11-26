class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp=[1]*len(nums)
        count=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
        max1=max(dp)
        return sum(c for l,c in zip(dp,count) if l==max1)
        
        