for i in range(1,5+1):
    for k in range(0,i):
        print(i,end="")
    print()
print("____________________________\n")
for i in range(1,5+1):
    for k in range(0,i):
        print(k+1,end="")
    print()
print("____________________________\n")
for i in range(1,5+1):
    for k in range(5+1,i,-1):
        print(i,end="")
    print()
print("_____________________________\n")
for i in range(1,5+1):
    j=1
    for k in range(5+1,i,-1):
        print(j,end="")
        j=j+1
    print()
print("____________________________\n")
