v=[]
q=[]
d={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}
def bfs(d,v,x):
    q.append(x)
    v.append(x)
    while q:
        a=q.pop(0)
        print(a,end=" ")
        for b in d[a]:
            if b not in v:
                bfs(d,v,b)
bfs(d,v,'A')