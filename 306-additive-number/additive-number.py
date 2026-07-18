class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break

            first = int(num[:i])

            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                second = int(num[i:j])
                a, b = first, second
                k = j

                while k < n:
                    c = a + b
                    s = str(c)

                    if not num.startswith(s, k):
                        break

                    k += len(s)
                    a, b = b, c

                if k == n:
                    return True

        return False