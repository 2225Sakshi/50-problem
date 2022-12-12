#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr.sort()
        return arr[k-1]
        

# //User function Template for Java

# class Solution{
#     public static int kthSmallest(int[] arr, int l, int r, int k) 
#     { 
#         //Your code here
#      { 

#         Arrays.sort(arr);

#         return arr[k-1];

#     } 

# }
# }
 
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends