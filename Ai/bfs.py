from queue import Queue
q=Queue()
p=Queue()
d={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
x='A'
def id(d,p,x):
    p.put(x)
    q.put(x)
    while q:
        a=q.get()
        print(a,end=" ")
        for b in d[a]:
            if b not in p.queue:
                p.put(b)
                q.put(b)
id(d,p,x)
