class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []

        for ch in s:
            if ch != "#":
                st1.append(ch)
            elif st1:
                st1.pop()

        for ch in t:
            if ch != "#":
                st2.append(ch)
            elif st2:
                st2.pop()

        return st1 == st2