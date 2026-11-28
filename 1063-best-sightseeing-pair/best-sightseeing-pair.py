class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        maxleft=values[0]
        ans=0
        for j in range(1,len(values)):
            ans=max(ans,maxleft+values[j]-j)
            maxleft=max(maxleft,values[j]+j)
        return ans