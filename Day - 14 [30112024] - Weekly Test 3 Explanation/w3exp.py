#Pattern - 1
#Approach - 1
'''
n = 5
for i in range(n):
    for j in range(n):
        if i==j or j == n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Approach - 2
'''
n = 5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Pattern - 2
#Approach - 2
'''
n = 5
for i in range(n):
    for j in range(n):
        if j<=i:
            if ((i==j) or ((i+j)%2)==0):
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Approach - 1
'''
n = 5
for i in range(n):
    if i%2 == 0:
        temp = 1
        for j in range(n):
            if i>=j:
                print(temp,end=" ")
                if temp == 1:
                    temp = 0
                else:
                    temp = 1
            else:
                print(" ",end=" ")
    else:
        temp = 0
        for j in range(n):
            if i>=j:
                print(temp,end=" ")
                if temp == 1:
                    temp = 0
                else:
                    temp = 1
            else:
                print(" ",end=" ")

    print()
'''
#Pattern - 3
#Approach - 1
'''
n = 5
for i in range(n):
    temp = 1
    for j in range(n):
        if (i==n-1 or j==0 or i==j):
            print(temp,end=" ")
            temp += 1
        else:
            print(" ",end=" ")
            temp += 1
    print()
'''
#Approach - 2
'''
n = 5
for i in range(n):
    for j in range(n):
        if (i==n-1 or j==0 or i==j):
            print(j+1,end=" ")
        else:
            print(" ",end=" ")
    print()
'''
        












