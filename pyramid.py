for i in range(1,5+1):
    for k in range(0,i):
        print("*",end="")
    print()
print("____________________________,\n")
for i in range(1,5+1):
    for k in range(5+1,i,-1):
        print("*",end="")
    print()
print("____________________________,\n")
for i in range(1,5+1):
    for k in range(0,i):
        print("*",end="")
    print()
for i in range(1,5+1):
    for k in range(5+1,i,-1):
        print("*",end="")
    print()
print("____________________________,\n")

for i in range(1,5+1):
    for k in range(5,i,-1):
        # print(chr(65 + i), end="")
        print(" ",end="")
    for j in range(0,i):
        # print(chr(65+j),end="")
        print("*",end="")
    print()
for i in range(1,5+1):
    for k in range(0,i):
        print(" ",end="")
    for j in range(5,i,-1):
        # print(chr(64+i),end="")
        print("*",end="")
    print()
