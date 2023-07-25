import sys
sys.setrecursionlimit(10**9)

class Graph:
    def __init__(self,name):
        self.name=name
        self.family=list()
    def add_edge(self,next):
        self.family.append(next)

def DFS(node,weight):

    for family in node.family:
        if visited[family[0].name] == -1:
            visited[family[0].name]=weight+family[1]
            DFS(family[0],family[1]+weight)

num=int(sys.stdin.readline())
graph=[0] * (num+1)
weights=[0]*(num+1)

for i in range(1,num+1):
    graph[i]=Graph(i)

for _ in range(num-1):
    father,kid,weight=map(int,sys.stdin.readline().split())
    graph[father].add_edge([graph[kid],weight])
    graph[kid].add_edge([graph[father],weight])
    

visited=[-1]*(num+1)
visited[1]=0
DFS(graph[1],0)
node1=visited.index(max(visited))

visited=[-1]*(num+1)
visited[node1]=0
DFS(graph[node1],0)

print(max(visited))