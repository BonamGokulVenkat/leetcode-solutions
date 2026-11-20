class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        sum=0
        res=0
        for n in nums:
            sum+=n
            diff=sum-k
            res+=prefix.get(diff,0)
            prefix[sum]=1+prefix.get(sum,0)
        return res