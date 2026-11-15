class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1=set()
        left=0
        right=0
        ans=0
        while right<len(s):
            ch=s[right]
            while ch in set1:
                set1.remove(s[left])
                left+=1
            set1.add(ch)
            right+=1
            ans=max(ans,right-left)
        return ans