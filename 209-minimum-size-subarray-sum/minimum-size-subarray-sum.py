class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans=float("inf")
        currSum=0
        low=0
        high=0
        while high < len(nums):
            currSum+=nums[high]
            high+=1
            while currSum>=target:
                currWindow=high-low
                ans=min(currWindow,ans)
                currSum-=nums[low]
                low+=1
        return 0 if ans==float("inf") else ans