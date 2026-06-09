class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        if brightness>n:
            return -1
        res=0
        reqb=ceil(brightness/3)
        #merging
        intervals.sort()
        ints=[intervals[0]]
        i=1
        while i<len(intervals):
            s1,e1=ints[-1]
            s2,e2=intervals[i]
            if s2>=s1 and s2<=e1:
                ints.pop()
                ints.append([min(s1,s2,e1,e2),max(s1,s2,e1,e2)])    
            else:
                ints.append(intervals[i])    
            i+=1
        for s,e in ints:
            res+=reqb*(e-s+1)
        return res