
from sys import argv

'''
Using the Floyd-Warshall algorithm, implement a python code that takes 2 command line inputs:

1) Cost Adjacency Matrix => Matrix that will represent any graph cost adjacency matrix.

2) k => Integer that will represent the matrix that your function will return, if zero it will 
   return the same cost adjacency matrix, if 1 the Floy Warshall matrix at node 1, etc...

The function must return the K matrix of the Floyd-Warshall algorithm.  
You can leverage the Floyd-Warshall code shared on the class videos.

The first argument will be in the form of [[....],[.....],[...],...].  

Remember the cost adjacency matrix is a squared matrix. 

inf represents no connection between nodes.

The output format is expected to be the same as the input cost adjacency matrix: [[....],[.....],[...],...]
'''

def Floyd_Warshall(graph, k):
    
    CAM = graph #CAM = Cost Adjacency Matrix 
    getLen = len(CAM)
    
    for k in range(0, k):
        for i in range(0,getLen):
            for j in range(0,getLen):
                
                if CAM[i][j] == 'inf':
                    CAM[i][j] = float('inf')
                    
                    
                CAM[i][j] = min( CAM[i][j], CAM[i][k]+ CAM[k][j])
    return CAM



if len(argv) > 1:

    graph = eval( argv[1].replace("inf","'inf'"))
    
    if len(argv) > 2:
        
        k = int(argv[2])
        
        print(Floyd_Warshall(graph, k))

    else: 
        print(Floyd_Warshall(graph, len(graph)))

###############################################
'''

def FloydWarshall(graph):
    n = len(graph)
    A = graph

    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    return A

pos_inf = float('inf')
graphA_0 = [[0,3,pos_inf,7],
        [8,0,2,pos_inf],
        [5,pos_inf,0,1],
        [2,pos_inf,pos_inf,0]]

print(FloydWarshall(graphA_0))

'''