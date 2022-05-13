class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        Scount = {}
        Tcount = {}
        
        for i in range(len(s)):
            Scount[s[i]] = Scount.get(s[i],0) + 1            
            Tcount[t[i]] = Tcount.get(t[i],0) + 1
            
        print(Scount)
        print(Tcount)

        if Scount == Tcount:
            return True
        else:
            return False
            
        