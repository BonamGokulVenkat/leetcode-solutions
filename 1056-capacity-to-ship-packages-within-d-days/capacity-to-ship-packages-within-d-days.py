class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left=0
        right=0
        for n in weights:
            left=max(left,n)
            right+=n
        while left<right:
            mid=left+(right-left)//2
            carry=0
            D=1
            for w in weights:
                if carry+w > mid:
                    D+=1
                    carry=0
                carry+=w
            if D>days:
                left=mid+1
            else:
                right=mid
        return left