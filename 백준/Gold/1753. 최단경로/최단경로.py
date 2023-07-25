import sys
import heapq as h

### heapQ(힙큐)를 이용한 다익스트라 알고리즘 구현 ###

def dijkstra(v_start):
    q=[]
    h.heappush(q,(0,v_start))
    distLst[v_start]=0

    while q:
        dist,node=h.heappop(q)
        if distLst[node]<dist:
            continue
        for weight,edge in graph[node]:
            cost=distLst[node]+weight
            if cost<distLst[edge]:
                distLst[edge]=cost
                h.heappush(q,(cost,edge))

inf=int(1e9)

v_num,e_num=map(int,sys.stdin.readline().split())
v_start=int(sys.stdin.readline())

distLst=[inf]*(v_num+1)

# 가중치 그래프 구현 #
graph=[[] for _ in range(v_num+1)]

for i in range(e_num):
    edge1,edge2,weight=map(int,sys.stdin.readline().split())
    graph[edge1].append((weight,edge2))

dijkstra(v_start)


for i in range(1,len(distLst)):
    if distLst[i]==inf:
        print('INF')
    else:
        print(distLst[i])
