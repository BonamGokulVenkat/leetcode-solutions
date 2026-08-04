class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, parts, path):
            if parts == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start + length]

                if len(segment) > 1 and segment[0] == '0':
                    continue

                if int(segment) > 255:
                    continue

                path.append(segment)
                backtrack(start + length, parts + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res