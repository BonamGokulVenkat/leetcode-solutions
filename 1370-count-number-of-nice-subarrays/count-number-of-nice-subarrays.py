class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(k):
            if k<0: return 0
            l=ans=sum=0
            for r in range(len(nums)):
                sum+=nums[r]%2
                while sum>k:
                    sum-=nums[l]%2
                    l+=1
                ans+=r-l+1
            return ans
        return atMost(k)-atMost(k-1)