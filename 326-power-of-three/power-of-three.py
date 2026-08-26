class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        return self.help(n)
    def help(self,n):
        if n==1:
            return True
        if n%3!=0:
            return False
        return self.help(n//3)