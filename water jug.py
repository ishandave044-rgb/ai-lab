def b(a):
    if a==1:
        print("4,0\n1,3\n1,0")
    elif a==2: 
        print("4,0\n1,3\n0,1\n4,1\n2,3\n2,0")
    else:
        print(3)

a=int(input("Enter Quantity: "))

if a%3==0:
    for i in range(int(a/3)):
        print(3)
elif a%4==0:
    for i in range(int (a/4)):
        print(4)
elif a>4 and a%4!=0:
    for i in range(int (a/4)):
        print(4)
    b(a%4)
else:
    if a==1:
        print("4,0\n1,3\n 1,0")
    if a==2:
        print("4,0\n1,3\n0,1\n4,1\n2,3\n2,0")
