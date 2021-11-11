w,h,x,y=input().split()
w=int(w)
h=int(h)
x,y=int(x),int(y)

area=w*h/2

count =0
if w==2*x and h ==2*y:
    count=1

print('{:.6f} {}'.format(area,count))
        