#User function Template for python3

class Solution:
	def canPair(self, nuns, k):
	   # for i in range(0,arr[i+1]):
	   #     for j in range(1,arr[j+1]):
	   #         if arr[i]+arr[j]%k==0:
	   #             return True 
	   #         return False
		# Code here
		if len(nuns)%2!=0:
            return False
        freq=[0]*k
        for i in nuns:
            r=i%k
            freq[r]+=1
        if freq[0]%2!=0:
            return False
        for r in range(1,k//2+1):
            if freq[r]!=freq[k-r]:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends