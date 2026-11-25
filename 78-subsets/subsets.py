class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        def find(idx,curr,ans):
            if idx==n:
                ans.append(curr.copy())
                return 
            curr.append(nums[idx])
            find(idx+1,curr,ans)
            curr.pop()
            find(idx+1,curr,ans)
        find(0,[],ans)
        return ans
