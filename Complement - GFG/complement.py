#User function Template for python3
class Solution:

	def findRange(self,a,size):
	    maxi=0
	    count=0
	   # st=0
	    l=0
	    res=[-1]
	    for r,ch in enumerate(a):
	        
	        if ch=='1':
	            count-=1
	        if ch == '0':
	            count+=1
            if count>maxi:
               maxi=count
               res=[l+1,r+1]
	        if count<0:
	            count=0
	            l=r+1
	    return res
	               
	            
	            
	    
    	# code here


#{ 
 # Driver Code Starts
if __name__ == '__main__': 


	tc=int(input())
	while tc > 0:
	    n=int(input())
	    s=input()
	    ob = Solution()
	    ans = ob.findRange(s, n)
	    if len(ans)==1:
	        print(ans[0])
	    else:
	        print(str(ans[0])+" "+str(ans[1]))
	    tc=tc-1
# } Driver Code Ends