class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen=dict()
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if rem in seen:
                return [i,seen[rem]]
            seen[nums[i]]=i
        return {-1,-1}
        