class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        sum=0
        res=0
        for num in nums:
            sum+=num
            diff=sum-k
            res+=prefixSum.get(diff,0)
            prefixSum[sum]=1+prefixSum.get(sum,0)
        return res