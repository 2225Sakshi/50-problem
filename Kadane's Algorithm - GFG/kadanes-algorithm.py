#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maximum=-99999999
        subarr_sum=0
        for i in range(N):
            subarr_sum = subarr_sum +arr[i]
            if subarr_sum > maximum:
                maximum = subarr_sum 
            if subarr_sum < 0:
                subarr_sum =  0
        return maximum
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends