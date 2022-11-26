def msquare(n):
    square=[[0 for x in range(n)]
                   for y in range(n)]
    i=n//2
    j=n-1
    num=1
    while num <= (n*n):
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
        if square[int(i)][int(j)]:
            j=j-2
            i=i+1
            continue
        else:
            square[int(i)][int(j)]=num
            num=num+1
        j=j+1
        i=i-1 
    print("Sum of each row or column:",n*(n*n+1)//2)
    print()
 
    for i in range(0,n):
        for j in range(0,n):
            print('%2d '% (square[i][j]),
                  end='')
            if j==n-1:
                print()
def DoublyEven(n):
    print("Sum of each row or column:",int((n*((n**2)+1))/2))
    print()
    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]
    for i in range(0,n//4):
        for j in range(0,n//4):
            arr[i][j] = (n*n + 1) - arr[i][j];
    for i in range(0,n//4):
        for j in range(3 * (n//4),n):
            arr[i][j] = (n*n + 1) - arr[i][j];
    for i in range(3 * (n//4),n):
        for j in range(0,n//4):
            arr[i][j] = (n*n + 1) - arr[i][j];
    for i in range(3 * (n//4),n):
        for j in range(3 * (n//4),n):
            arr[i][j] = (n*n + 1) - arr[i][j];
    for i in range(n//4,3 * (n//4)):
        for j in range(n//4,3 * (n//4)):
            arr[i][j] = (n*n + 1) - arr[i][j];
    for i in range(n):
        for j in range(n):
            print ('%2d ' %(arr[i][j]),end=" ")
        print()
def introduction():
    print()
    print("    𝓦𝓔𝓛𝓒𝓞𝓜𝓔!! ")
    print()
    m=int(input("Enter value for dimension:"))
    print()
    if m%2!=0:
        msquare(m)
    if m%2==0:
        if m%4==0:
            DoublyEven(m)
        else:
            print()
            print("Please enter any 𝓞𝓭𝓭 number or 𝓔𝓿𝓮𝓷 numbers 𝓓𝓲𝓿𝓲𝓼𝓲𝓫𝓵𝓮 by 𝟒 !!!!")
            a=input("Enter y to continue:")
            if a=="y" or a=="Y":
                introduction()
introduction()