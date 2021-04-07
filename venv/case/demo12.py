import  math
a=int(input("请输入："))
s=0
list=[]
for i in range(a):
    s+=int(int(a)*math.pow(10,i))
    list.append(s)
print(sum(list))

