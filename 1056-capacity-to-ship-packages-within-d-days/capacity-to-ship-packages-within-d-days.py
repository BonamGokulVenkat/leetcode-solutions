class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left=0
        right=0
        for w in weights:
            left=max(left,w)
            right+=w
        def possible(weight):
            sum=0
            d=1
            for w in weights:
                if sum+w>weight:
                    d+=1
                    sum=0
                sum+=w
            return d<=days
        while left<right:
            mid=left+(right-left)//2
            if possible(mid):
                right=mid
            else:
                left=mid+1
        return left