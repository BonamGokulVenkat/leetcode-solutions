class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        @lru_cache(None)
        def find(idx):
            if idx<0:
                return 0
            if idx==0:
                nums[idx]
            take=nums[idx]+find(idx-2)
            not_take=find(idx-1)
            return max(take,not_take)
        return find(n-1)
    