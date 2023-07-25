import sys

class Graph:
    def __init__(self,name):
        self.name=name
        self.edge=list()
    
    def add_edge(self,node):
        self.edge.append(node)

def DFS(node1,node2,visited):
    visited.append(node1.name)
    if node1==node2:
        return 1
    for edge in node1.edge:
        if edge.name not in visited:
            if DFS(edge,node2,visited) != 1:
                continue
            else:
                return 1
    return -1    

city=int(sys.stdin.readline()) #도시 개수
plans=int(sys.stdin.readline()) #여행할 도시 개수
connect=[]                      # 연결 상태 리스트
graph=[0] * (city+1)

for i in range(1,city+1):
    graph[i]=Graph(i)

for i in range(city):
    temp=list(map(int,sys.stdin.readline().split()))
    connect.append(temp)

plan=list(map(int,sys.stdin.readline().split()))

for i in range(city):
    for num,j in enumerate(connect[i]):
        if j == 1:
            graph[i+1].add_edge(graph[num+1])

'''
for gr in graph:
    if graph.index(gr)==0:
        continue
    for i in gr.edge:
        print(gr.name, ' : ' ,i.name)
'''
for i in range(len(plan)-1):
    visited=[]
    if DFS(graph[plan[i]],graph[plan[i+1]],visited)==-1:
        print('NO')
        sys.exit()

print('YES')
#그래프에 추가 후 for문 돌면서 0번 index 부터 -1 index까지 순차적으로 돌려서 다 갈 수 있는지.

