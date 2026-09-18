class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st=[]
        for i in operations:
            if i!='C' and i!='D' and i!='+':
                st.append(int(i))
            elif i=='D':
                v = st[-1]*2
                st.append(v)
            elif i=='C':
                st.pop()
            elif i=='+':
                v1, v2 = st[-1], st[-2]
                st.append(v1 + v2)
        return sum(st)