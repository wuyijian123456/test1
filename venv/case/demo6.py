import math
c=50
h=30
d=input("请输入个整数")
print(type(d))
t=d.split(',')
print(t)
list=[]
for i in t:
    d=int(i)
    s=2*c*d/h
    q=math.sqrt(s)
    m=round(q)
    list.append(m)
print((",".join(map(str,list))))

    #print(round(q))
    #print("{:.0f}".format(q),end=',')





