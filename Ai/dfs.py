q=[]
p=[]
d={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
x='A'
def id(d,p,x):
    p.append(x)
    q.append(x)
    while q:
        a=q.pop(0)
        print(a,end=" ")
        for b in d[a]:
            if b not in p:
                id(d,p,b)
id(d,p,x)
