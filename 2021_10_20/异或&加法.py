
n=input()

dy=1
xy=0


for i in range(len(n)):
    if n[i]=='0':
        xy=int(xy*3%(1e9+7))
    
    else:
        xy=int((xy*3+dy)%(1e9+7))
        dy=int(dy*2%(1e9+7))


print(int((xy+dy)%(1e9+7)))