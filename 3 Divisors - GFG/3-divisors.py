#User function Template for python3


class Solution:
	def threeDivisors(self, query, q):
		def prime_num(x):
            for k in range(2, x):
                if x % k == 0:
                    return False
            return True
        
        lst=[]
        D=0
        for i in query:
            if D:
                lst.append(D)
                D=0
            if i<4:
                lst.append(0)
            for j in range(1,int(i**0.5)+1):
                if prime_num(j):
                    if j**2<=i and j!=1:
                        D+=1
        if D>0:
            lst.append(D)
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends