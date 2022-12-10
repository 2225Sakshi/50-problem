#User function Template for python3

class Solution:

    def buildLowestNumber(self, S,N):
        stack= []
        for num in S:
            while N and stack and stack[-1]>num:
                stack.pop()
                N-=1
            stack.append(num)
        final = ''.join(stack[:len(stack)-N]).lstrip('0')
        return "0" if not final else final
        
        # stack = []

        # for i in range(len(S)):
        #     num = int(S[i])

        #     while stack and N>0 and num<stack[-1]:
        #         stack.pop()
        #         N-=1
        #     stack.append(num)
        
        # # while stack and N>0:
        # #     stack.pop()
        # #     N-=1
        
        # res=  "".join([str(i) for i in stack])
        # return str(int(res))
        
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends