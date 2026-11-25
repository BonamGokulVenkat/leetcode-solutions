class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        def find(idx,curr):
            if idx==n:
                ans.append(curr.copy())
                return 
            curr.append(nums[idx])
            find(idx+1,curr)
            curr.pop()
            find(idx+1,curr)
        find(0,[])
        return ans
