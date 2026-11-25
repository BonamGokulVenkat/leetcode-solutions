class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def find(low,high):
            @lru_cache(None)
            def find1(idx):
                if idx<low:
                    return 0
                if idx==low:
                    return nums[idx]
                take=nums[idx]+find1(idx-2)
                not_take=find1(idx-1)
                return max(take,not_take)
            return find1(high)
        return max(find(0,n-2),find(1,n-1))
