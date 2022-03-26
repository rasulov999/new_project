

n=int(input("n= "))
for i in range(n+1):
    for t in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()