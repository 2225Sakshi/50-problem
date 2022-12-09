#User function Template for python3


#Function to find out the number of ways we can place a black and a white
#Knight on this chessboard such that they cannot attack each other.
def numOfWays(M, N):
    ans=0
    squares=N*M
    for i in range(N):
        for j in range(M):
            curr=squares-1
            if -1<i-2<N:
                if -1<j-1<M:
                    curr-=1
                if -1<j+1<M:
                    curr-=1
            if -1<i-1<N:
                if -1<j-2<M:
                    curr-=1
                if -1<j+2<M:
                    curr-=1
            if -1<i+1<N:
                if -1<j-2<M:
                    curr-=1
                if -1<j+2<M:
                    curr-=1
            if -1<i+2<N:
                if -1<j-1<M:
                    curr-=1
                if -1<j+1<M:
                    curr-=1
            ans=(ans+curr)%(10**9+7)
    return ans
    
    
    
    mod=1000000007
    res=[]
    for i in range(N):
        for j in range(M):
            count=M*N-1
            if (i-2>=0 and j-1>=0):
                count-=1
            if (i-2>=0 and j+1<=N):
                count-=1
            if (i-1>=0 and j+2<=N):
                count-=1
            if (i+1 <=M and j+2<N):
                count-=1
            if (i+2<=M and j+1<=N):
                count-=1
            if (i+2<=M and j+1>=N):
                count-=1
            if (i+1<=M and j-2>=0):
                count-=1
            if (i-1>=0 and j-2>=0):
                count-=1
            
            res=((res+count)%mod)
    return res
            
    
        
    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m,n = map(int,input().strip().split())
        print(numOfWays(m,n))

# } Driver Code Ends