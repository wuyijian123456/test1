a=input("请输入：")

list=[]
for i in a.split(","):
    i=int(i)
    if i%2!=0:
        list.append(str(i))
print(','.join(list))

