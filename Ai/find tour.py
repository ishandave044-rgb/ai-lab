l=['jodhpur','ajmer','alwar','bikaner','nagaur']
print(l)
l1=[]
d={0:[150,300,280,90],1:[150,270,120,100],2:[300,270,400,110],3:[280,120,400,130],4:[90,100,110,130]}
n=input("enter destination..")
x=l.index(n)
q=0
l1.append(l[x])
for i in range (2):
    p=d[x]
    if q in p:
        p.remove(q)
    q=min(p)
    l1.append(l[p.index(q)+1])
    x=p.index(q)+1
print(f"{l1[0]} to {l1[1]} to {l1[2]}")
