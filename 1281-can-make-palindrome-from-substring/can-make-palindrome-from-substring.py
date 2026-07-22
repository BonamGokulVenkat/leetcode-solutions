class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)

        prefix = [0] * (n + 1)

        mask = 0
        for i, ch in enumerate(s):
            mask ^= 1 << (ord(ch) - ord('a'))
            prefix[i + 1] = mask

        ans = []

        for l, r, k in queries:
            mask = prefix[r + 1] ^ prefix[l]

            odd = mask.bit_count()

            ans.append(odd // 2 <= k)

        return ans