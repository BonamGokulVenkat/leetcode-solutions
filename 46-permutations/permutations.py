class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        curr=[]
        n=len(nums)
        used=[False]*n
        def dfs():
            if len(curr)==len(nums):
                ans.append(curr.copy())
                return
            for i in range(n):
                if used[i]==True:
                    continue
                used[i]=True
                curr.append(nums[i])
                dfs()
                curr.pop()
                used[i]=False
        dfs()
        return ans