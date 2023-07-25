import sys

def BFS(x,y):
    global init__
    q=set([(x,y,maze[x][y])])
    while q:
        x,y,ans=q.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<r) and (0<=ny<c):
                if maze[nx][ny] not in ans:
                    q.add((nx,ny,ans+maze[nx][ny]))
                    init__=max(init__,len(ans)+1)
#남 동 북 서 순서
dx=[0,1,0,-1]
dy=[1,0,-1,0]
r,c=map(int,sys.stdin.readline().split())
maze=[]

for i in range(r):
    maze.append(list(sys.stdin.readline().strip()))

init__=1
BFS(0,0)
print(init__)