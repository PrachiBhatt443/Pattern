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
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end=’ ‘)
    print(“”)
print("____________________________\n")
rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=’ ‘)
    print(‘\r’)
print("____________________________\n")


