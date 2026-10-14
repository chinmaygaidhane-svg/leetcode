class Solution:
    def isValid(self, s: str) -> bool:
        # A valid string cannot have an odd length
        if len(s) % 2 != 0:
            return False

        st = []

        for ch in s:
            if ch in '({[':
                st.append(ch)
            else:
                if not st:
                    return False
                top = st.pop()
                if ch == ')' and top != '(':
                    return False
                elif ch == '}' and top != '{':
                    return False
                elif ch == ']' and top != '[':
                    return False

        return len(st) == 0