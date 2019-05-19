import math
dice,point=map(int,input().split())
percent = 0.0
power = 0
for i in range(1,dice+1):
    for j in range(20):
        if (point <= i *(2 **j)):
            power = j
            break


    current = (1 / dice) * (1/2) ** power
    percent = percent + current


print(percent)
