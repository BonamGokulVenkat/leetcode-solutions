class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        leftRemove = rightRemove = 0

        for ch in s:
            if ch == '(':
                leftRemove += 1
            elif ch == ')':
                if leftRemove > 0:
                    leftRemove -= 1
                else:
                    rightRemove += 1

        ans = set()

        def dfs(i, path, leftRemove, rightRemove, openCount):
            if openCount < 0:
                return

            if i == len(s):
                if leftRemove == 0 and rightRemove == 0 and openCount == 0:
                    ans.add(path)
                return

            ch = s[i]

            if ch == '(':
                if leftRemove > 0:
                    dfs(i + 1, path, leftRemove - 1, rightRemove, openCount)

                dfs(i + 1, path + '(', leftRemove, rightRemove, openCount + 1)

            elif ch == ')':
                if rightRemove > 0:
                    dfs(i + 1, path, leftRemove, rightRemove - 1, openCount)

                if openCount > 0:
                    dfs(i + 1, path + ')', leftRemove, rightRemove, openCount - 1)

            else:
                dfs(i + 1, path + ch, leftRemove, rightRemove, openCount)

        dfs(0, "", leftRemove, rightRemove, 0)

        return list(ans)