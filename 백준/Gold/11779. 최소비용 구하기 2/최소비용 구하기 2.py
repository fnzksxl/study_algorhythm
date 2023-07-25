import sys
import heapq
inf=sys.maxsize

def dijkstra(start):
    distlst=[inf] * (n+1)
    citylst=[[] for _ in range(n+1)]
    q=[]
    heapq.heappush(q,(start,0))
    distlst[start]=0
    citylst[start].append(start)
    while q:
        node,dist=heapq.heappop(q)
        if distlst[node]<dist:
            continue
        for next,weight in graph[node]:
            cost=distlst[node]+weight
            if cost<distlst[next]:
                distlst[next]=cost
                citylst[next]=citylst[node]+[next]
                heapq.heappush(q,(next,cost))

    return distlst[end],len(citylst[end]),citylst[end]
    

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    start,end,weight=map(int,sys.stdin.readline().split())
    graph[start].append((end,weight))

start,end=map(int,sys.stdin.readline().split())

cost,length,way=dijkstra(start)

print(cost)
print(length)
print(*way)