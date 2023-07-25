import sys
import heapq
inf=sys.maxsize

def dijkstra(start):
    distlst=[inf] * (n+1)
    q=[]
    heapq.heappush(q,(start,0))
    distlst[start]=0

    while q:
        node,dist=heapq.heappop(q)
        if distlst[node]<dist:
            continue
        for next,weight in graph[node]:
            cost=distlst[node]+weight
            if cost<distlst[next]:
                distlst[next]=cost
                heapq.heappush(q,(next,cost))    
    
    return max(distlst[1:]),distlst.index(max(distlst[1:]))

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for _ in range(n):
    now=list(map(int,sys.stdin.readline().split()))
    for i in range(1,len(now)-1,2):
        graph[now[0]].append((now[i],now[i+1]))

_,idx=dijkstra(1)
ans,_=dijkstra(idx)

print(ans)


