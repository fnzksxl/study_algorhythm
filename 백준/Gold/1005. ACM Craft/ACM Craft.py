import sys
from collections import deque

T=int(sys.stdin.readline())
for case in range(T):
    n,k=map(int,sys.stdin.readline().split())
    rule=[[] for _ in range(n+1)]
    time=[0] + list(map(int,sys.stdin.readline().split()))
    inDegree=[0 for _ in range(n+1)]
    dp=[0 for _ in range(n+1)]

    for _ in range(k):
        start,end=map(int,sys.stdin.readline().split())
        rule[start].append(end)
        inDegree[end]+=1

    q=deque()
    for i in range(1,n+1):
        if inDegree[i]==0:
            q.append(i)
            dp[i]=time[i]

    while q:
        a=q.popleft()
        for i in rule[a]:
            inDegree[i]-=1
            dp[i]=max(dp[a]+time[i],dp[i])
            if inDegree[i]==0:
                q.append(i)

    w=int(sys.stdin.readline())
    print(dp[w])