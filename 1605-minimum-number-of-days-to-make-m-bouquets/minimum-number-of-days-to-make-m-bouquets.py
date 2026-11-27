class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def possible(Days):
            b=0
            f=0
            for day in bloomDay:
                if day<=Days:
                    f+=1
                    if f==k:
                        b+=1
                        f=0
                else:
                    f=0
            return b>=m
        left,right=min(bloomDay),max(bloomDay)
        while left<right:
            mid=left+(right-left)//2
            if possible(mid):
                right=mid
            else:
                left=mid+1
        return left