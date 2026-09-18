class Solution:
    def isValid(self, s: str) -> bool:
        open_b = "({["
        close_b = ")}]"
        d=dict(zip(close_b, open_b))
        st = []
        for i in s:
            if i in open_b:
                st.append(i)
            else:
                if not st:
                    return False
                else:
                    if d[i] == st[-1]:
                        st.pop()
                    else:
                        return False
        return not st