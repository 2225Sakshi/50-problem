#User function Template for python3


class Solution:
    def firstElementKTime(self,  a, n, k):
        arr=[0]*1000
        count=0
        for i in range(n):
            arr[a[i]]+=1
            if arr[a[i]]==k:
                return(a[i])
        if k not in arr:
            return(-1)
        
        # code here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends