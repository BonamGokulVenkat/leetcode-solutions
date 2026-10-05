class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen=list()
        for ch in s:
            seen.append(ch)
        for ch in t:
            if ch in seen:
                seen.remove(ch)
            else: return False
        if len(seen)!=0: return False
        return True