def tapis(n):
    for i in range(n+1):

        for j in range (n+1):
            if j==i:
                print(" ",end="")
            else:
               print("#",end="")
        print()

tapis(10)