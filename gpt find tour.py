l = ['jodhpur','ajmer','alwar','bikaner','nagaur']
print(l)

# distance matrix properly aligned
d = {
    0:[0,150,300,280,90],
    1:[150,0,270,120,100],
    2:[300,270,0,400,110],
    3:[280,120,400,0,130],
    4:[90,100,110,130,0]
}

n = input("enter destination.. ")
x = l.index(n)

visited = [x]

for _ in range(2):
    dist_list = d[x]         # copy list
    for v in visited:           # already visited ko ignore karo
        dist_list[v] = 999999
    next_city = dist_list.index(min(dist_list))
    visited.append(next_city)
    x = next_city

print(" → ".join(l[i] for i in visited))


