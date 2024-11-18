N=7
arr=[[1 if j==0 or j%2==0 else 0 for i in range(N)] for j in range(N)]
for res in arr:
    print (*res)