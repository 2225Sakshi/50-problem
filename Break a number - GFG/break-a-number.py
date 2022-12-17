#User function Template for python3


class Solution:
    def waysToBreakNumber(self, n):
        mod=1000000007
        res=((n+1)%mod * (n+2)%mod) %mod //2
        return res
        # count=0
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if (i+j+k)==n:
        #                 count+=1
        # return count
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        print(ob.waysToBreakNumber(n))
        
# } Driver Code Ends