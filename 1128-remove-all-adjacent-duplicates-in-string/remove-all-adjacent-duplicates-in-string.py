class Solution(object):
    def removeDuplicates(self, s: str) -> str:
        st = []

        for ch in s:
            # If current character matches the top of the stack, remove the adjacent pair
            if st and st[-1] == ch:
                st.pop()
            else:
                st.append(ch)

        # Reconstruct the string from the remaining characters
        return "".join(st)