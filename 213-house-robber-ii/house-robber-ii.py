class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        @lru_cache(None)
        def find(low,idx):
            if idx<low:
                return 0
            if idx==low:
                return nums[idx]
            take=nums[idx]+find(low,idx-2)
            not_take=find(low,idx-1)
            return max(take,not_take)
        return max(find(0,n-2),find(1,n-1))
