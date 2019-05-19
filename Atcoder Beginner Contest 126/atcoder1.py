a,b=map(int,input().split())
c = input()



d=a-b+1
c = list(c)
d = c[b-1]
c[b-1] = d.lower()

c = "".join(c)
print(c)
