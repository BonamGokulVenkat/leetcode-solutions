class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        right=0
        for p in piles:
            right=max(right,p)
        left=1
        while left<=right:
            mid=left+(right-left)//2
            if self.can(piles,h,mid):
                right=mid-1
            else:
                left=mid+1
        return left
    def can(self,piles,h,mid):
        hours=0
        for p in piles:
            hours+=(p+mid-1)//mid
        return h>=hours
    