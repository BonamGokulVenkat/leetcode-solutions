class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sum=0
        n=len(nums)
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        res=0
        for i,n in enumerate(nums):
            prefix_sum=prefix_sum+n
            rem=prefix_sum%k
            res+=prefix_count[rem]
            prefix_count[rem]+=1
        return res
