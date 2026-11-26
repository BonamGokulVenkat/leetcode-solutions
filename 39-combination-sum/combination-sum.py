class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        n=len(candidates)
        def dfs(idx,curr,target):
            if idx==n:
                if target==0:
                    res.append(curr.copy())
                return
            if candidates[idx]<=target:
                curr.append(candidates[idx])
                dfs(idx,curr,target-candidates[idx])
                curr.pop()
            dfs(idx+1,curr,target)
        dfs(0,[],target)
        return res