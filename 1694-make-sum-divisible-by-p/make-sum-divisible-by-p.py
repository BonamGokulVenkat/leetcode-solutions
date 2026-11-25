class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total=sum(nums)
        target=total%p
        if target==0:
            return 0
        n=len(nums)
        prefix={0:-1}
        sum1=0
        min1=n
        for i,num in enumerate(nums):
            sum1=(sum1+num)%p
            rem=(sum1-target)%p
            if rem in prefix:
                min1=min(min1,i-prefix[rem])
            prefix[sum1]=i
        return min1 if min1<n else -1