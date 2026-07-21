class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = ""
        right = ""

        i = 0
        j = len(text) - 1

        ans = 0

        while i <= j:
            left += text[i]
            right = text[j] + right

            if left == right:
                if i == j:
                    ans += 1
                else:
                    ans += 2

                left = ""
                right = ""

            i += 1
            j -= 1

        if left:
            ans += 1

        return ans