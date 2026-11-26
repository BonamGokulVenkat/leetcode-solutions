class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n=len(candidates)
        candidates.sort()
        res=[]
        def dfs(idx,curr,target):
            if target==0:
                res.append(curr.copy())
                return
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                curr.append(candidates[i])
                dfs(i+1,curr,target-candidates[i])
                curr.pop()
        dfs(0,[],target)
        return res

