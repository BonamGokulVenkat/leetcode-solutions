class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        def dfs(idx,curr):
            if idx==n:
                res.append(curr.copy())
                return
            curr.append(nums[idx])
            dfs(idx+1,curr)
            curr.pop()
            dfs(idx+1,curr)
        dfs(0,[])
        return res