class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first=self.search(nums,target,True)
        last=self.search(nums,target,False)
        return [first,last]
    def search(self,nums,target,first):
        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                ans=mid
                if first:
                    r=mid-1
                else:
                    l=mid+1
        return ans
