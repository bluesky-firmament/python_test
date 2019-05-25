import numpy as np
n,m=map(int,input().split())
a = np.array(input().split(),dtype=np.int64)
for i in range(m):
    a = np.sort(a)
    b,c=map(int,input().split())
    for j in range(b):
        if a[:j+1].sum()<c*(j+1):
            a[:j+1] = c 
print(a.sum())
