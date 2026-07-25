class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1

        for ch in s:
            if ch.isdigit():
                digit = int(ch)

                if digit > first:
                    second = first
                    first = digit
                elif second < digit < first:
                    second = digit

        return second