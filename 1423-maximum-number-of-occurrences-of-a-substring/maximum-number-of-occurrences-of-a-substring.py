class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)
        count = defaultdict(int)

        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            if right - left + 1 > minSize:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            if right - left + 1 == minSize and len(freq) <= maxLetters:
                sub = s[left:right + 1]
                count[sub] += 1

        return max(count.values(), default=0)