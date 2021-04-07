import math
a= input("请输入：")
b=a.split(",")
s=0
list1=[]
for i in b:
    if len(i)!=4:
        break;
    else:
        h=list(i)
        for c in h:
            t=h.index(c)
            s+=int(c)*math.pow(2,3-t)
        print(s)
        list1.append(s)
print(list1)
# for d in list1:
#     if d%5==0:
#         print(b[list1.index(d)])
#     else:
#         print(d)








