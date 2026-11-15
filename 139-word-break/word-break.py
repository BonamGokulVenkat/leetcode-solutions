class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        set1=set(wordDict)
        maxlen=0
        dp=[False]*(len(s)+1)
        dp[0]=True
        for s1 in set1:
            maxlen=max(maxlen,len(s1))
        for i in range(1,len(s)+1):
            for j in range(i-1,max(0,i-maxlen)-1,-1):
                if dp[j] and s[j:i] in set1:
                    dp[i]=True
                    break
        return dp[len(s)]