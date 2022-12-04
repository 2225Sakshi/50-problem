#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color=[0]*V
    def mcolor(vertex,graph,k,V):
        if vertex==V:
            return True
        
        for i in range(1,k+1):
            flag=1
            for j in range(V):
                if graph[vertex][j]==1 and color[j]==i:
                    flag=0
                    break
                
            if flag==1:
                    color[vertex]=i
                    if mcolor(vertex+1,graph,k,V):
                        return True
                    
                    color[vertex]=0
        return False
        
    return mcolor(0,graph,k,V)
            
    
    #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends