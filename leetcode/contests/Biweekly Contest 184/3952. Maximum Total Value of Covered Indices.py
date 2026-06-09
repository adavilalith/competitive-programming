class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n=len(nums)
        dp=[[0,0,0] for i in range(n)] # take, take prev, dont take
        if s[0]=='1':
            dp[0][0]=nums[0]
        for i in range(1,n):
            if s[i]=='1':
                dp[i][0]=nums[i]+max(dp[i-1])
                dp[i][1]=nums[i-1]+max(dp[i-1][1],dp[i-1][2])
            dp[i][2]=max(dp[i-1])
        return max(dp[-1])                