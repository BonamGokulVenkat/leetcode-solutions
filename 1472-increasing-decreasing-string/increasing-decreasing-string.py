class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        res = []

        while len(res) < len(s):
            for c in range(26):
                ch = chr(c + ord('a'))
                if count[ch]:
                    res.append(ch)
                    count[ch] -= 1

            for c in range(25, -1, -1):
                ch = chr(c + ord('a'))
                if count[ch]:
                    res.append(ch)
                    count[ch] -= 1

        return "".join(res)