class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        farthest=0
        curr_end=0
        ans=0
        for i in range(n-1):
            farthest=max(farthest,nums[i]+i)
            if i==curr_end:
                ans+=1
                curr_end=farthest
                if curr_end>=n-1:
                    break
        return ans