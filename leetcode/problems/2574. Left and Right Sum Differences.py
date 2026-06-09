class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        pre=[0]*(n+1)
        suf=[0]*(n+1)
        for i in range(1,n):
            pre[i]=nums[i-1]+pre[i-1]
        for i in range(n-2,-1,-1):
            suf[i]=nums[i+1]+suf[i+1]
        for i in range(n):
            res.append(abs(pre[i]-suf[i]))
        return res
        