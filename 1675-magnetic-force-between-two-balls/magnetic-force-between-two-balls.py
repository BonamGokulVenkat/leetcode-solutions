class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        def possible(mid):
            cnt=1
            prev=position[0]
            for p in position:
                if p-prev>=mid:
                    prev=p
                    cnt+=1
                    if cnt==m:
                        return True
            return False
        l,r=1,position[-1]-position[0]
        ans=1
        while l<=r:
            mid=l+(r-l)//2
            if possible(mid):
                l=mid+1
                ans=mid
            else:
                r=mid-1
        return ans
