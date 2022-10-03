Q1 .Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.




Sol: 

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
