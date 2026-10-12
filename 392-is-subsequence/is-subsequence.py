class Solution(object):
    def isSubsequence(self, s, t):
        c = []
        j = 0

        for i in s:
            while j < len(t):
                if i == t[j]:
                    c.append(i)
                    j += 1
                    break
                j += 1

        return c == list(s)