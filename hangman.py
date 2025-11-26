w="hangman"
l=list(w)
l1=['*','*','*','*','*','*','*']
c=0
for i in range(len(l)*2):
    g=input("guess the word: ")
    for j in range(len(l)):
        if g==l[j]:
            l1[j]=g
            c+=1
    print(l1)
    print(len(l)*2-i,"attemps left")
    if c==len(l):
        print("You Win")
        break
    if i==(len(l)*2-1):
        print("You Lose")
        