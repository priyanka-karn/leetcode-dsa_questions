class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        # i is index in s, j is index in p
        @cache
        def dfs(i,j):
            # reached both string and pattern ends - matched
            if i >= n and j >= m:
                return True

            # reached pattern end but not string end - not matched
            if j >= m:
                return False

            # match characters under i and j indexes (plus additional check whether we reached end of string), move both indexes forward
            if i < n and (s[i] == p[j] or p[j] == "?"):
                return dfs(i + 1, j + 1)

            # for wildcard there are two options:
            #   1) use it and move i forward (plus additional check whether we reached end of string)
            #   2) do not use it and move j forward
            if (p[j] == "*"):
                return (i < n and dfs(i + 1, j)) or dfs(i, j + 1)

            # no wildcard and not matched (or reached end of string before reaching end of pattern)
            return False

        return dfs(0,0)
