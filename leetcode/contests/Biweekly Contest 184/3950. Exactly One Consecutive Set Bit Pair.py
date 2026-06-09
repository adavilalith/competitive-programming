class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b=bin(n)[2:]
        res=0
        for i in range(len(b)-1):
            if b[i]=='1' and b[i+1]=='1':
                res+=1
        return res==1