class Solution:
    def fib(self, n: int) -> int:
        dp=[0]*(n+1) 
        return self.fib1(dp,n)
    def fib1(self,dp, n:int) -> int:
        if n<=1:
            return n
        if dp[n]!=0:
            return dp[n]
        dp[n-1]=self.fib1(dp,n-1)
        dp[n-2]=self.fib1(dp,n-2)
        return dp[n-1]+dp[n-2]

        