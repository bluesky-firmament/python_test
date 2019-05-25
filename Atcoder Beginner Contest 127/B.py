r,d,x=map(int,input().split())
post = x
for i in range(10):
    post= r * post -d
    print(post)
