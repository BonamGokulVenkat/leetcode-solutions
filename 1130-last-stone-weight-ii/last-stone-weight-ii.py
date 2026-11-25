class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total=sum(stones)
        target=total//2
        n=len(stones)
        @lru_cache(None)
        def find(idx,target):
            if target==0:
                return True
            if idx<0 or target<0:
                return False
            take=find(idx-1,target-stones[idx])
            not_take=find(idx-1,target)
            return take or not_take
        for s in range(target,-1,-1):
            if find(n-1,s):
                return total-2*s
        return total