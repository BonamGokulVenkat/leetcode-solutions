class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getValue(word):
            num = 0
            for ch in word:
                num = num * 10 + (ord(ch) - ord('a'))
            return num

        return getValue(firstWord) + getValue(secondWord) == getValue(targetWord)