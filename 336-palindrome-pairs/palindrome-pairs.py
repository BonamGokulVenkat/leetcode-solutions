class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s):
            return s == s[::-1]

        word_to_index = {word: i for i, word in enumerate(words)}
        ans = []

        for i, word in enumerate(words):

            for j in range(len(word) + 1):

                left = word[:j]
                right = word[j:]

                # Case 1
                if isPalindrome(left):
                    rev = right[::-1]
                    if rev in word_to_index and word_to_index[rev] != i:
                        ans.append([word_to_index[rev], i])

                # Case 2
                if j != len(word) and isPalindrome(right):
                    rev = left[::-1]
                    if rev in word_to_index and word_to_index[rev] != i:
                        ans.append([i, word_to_index[rev]])

        return ans