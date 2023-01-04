
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        # l=[]
        # for i in range(N):
        #     flag=1
        #     for j in range(i+1,N):
        #         if A[i]>=A[j]:
        #             continue
        #         else:
        #             flag=0
        #             break
        #     if flag==1:
        #         l.append(A[i])
        # return l
        
        mx=0
        l=[]
        for i in range(N-1,-1,-1):
            if A[i]>=mx:
                l.append(A[i])
                mx=A[i]
        return l[::-1]
            
        
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends