import sys
import heapq

def dijkstra(start,end):
    distLst=[inf]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    distLst[start]=0

    while q:
        dist,node=heapq.heappop(q)
        if distLst[node]<dist:
            continue
        for weight,edge in graph[node]:
            cost=distLst[node]+weight
            if cost<distLst[edge]:
                distLst[edge]=cost
                heapq.heappush(q,(cost,edge))
    return distLst[end]
        
inf=sys.maxsize
n,e=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for _ in range(e):
    e1,e2,weight=map(int,sys.stdin.readline().split())
    graph[e1].append((weight,e2))
    graph[e2].append((weight,e1))

v1,v2=map(int,sys.stdin.readline().split())

path1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
path2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)

if path1 >= inf and path2>= inf:
    print(-1)
else:
    print(min(path1,path2))