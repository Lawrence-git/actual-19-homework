for i in range(1,10):
    for n in range (1,10):
        j=i*n
        if i>=n:
         print('{}*{}={}'.format(i,n,j),end=" ")
    print()