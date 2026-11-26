class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        def dfs(idx,curr):
            res.append(curr.copy())
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                dfs(i+1,curr)
                curr.pop()
        dfs(0,[])
        return res