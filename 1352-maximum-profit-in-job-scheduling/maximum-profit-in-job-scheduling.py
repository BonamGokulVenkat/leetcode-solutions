class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        intervals=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
        endTimes=[x[1] for x in intervals]
        n=len(intervals)
        dp=[0]*(n+1)

        for i in range(1,len(intervals)+1):
            s,e,p=intervals[i-1]
            j=bisect_right(endTimes,s,0,len(intervals)-1)
            dp[i]=max(dp[i-1],dp[j]+p)
        return dp[n]