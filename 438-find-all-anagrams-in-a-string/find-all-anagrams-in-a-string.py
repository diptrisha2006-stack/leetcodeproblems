class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        d={}
        t={}
        l=0
        a=[]
        for i in p:
            t[i]=t.get(i,0)+1
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            if r>=k-1:
                if d==t:
                    a.append(l)
                d[s[l]]-=1
                if d[s[l]]==0:
                    d.pop(s[l])
                l+=1    
        return a