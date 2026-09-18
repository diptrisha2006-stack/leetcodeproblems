class Solution:
    def isValid(self, s: str) -> bool:
        open_b = "({["
        close_b = ")}]"
        st = []
        for i in s:
            if i in open_b:
                st.append(i)
            else:
                if not st:
                    return False
                else:
                    if i==')' and st[-1] == '(' or i=='}' and st[-1] == '{' or i==']' and st[-1] == '[':
                        st.pop()
                    else:
                        return False
        return not st