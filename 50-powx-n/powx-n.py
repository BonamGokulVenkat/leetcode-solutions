class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/self.solve(x,-n)
        return self.solve(x,n)
    def solve(self, x,n):
        if n==0:
            return 1
        if x==0:
            return 0
        res=self.solve(x,n//2)
        if n%2==0:
            return res*res
        
        return res*res*x
        