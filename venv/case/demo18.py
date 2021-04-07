from operator import itemgetter, attrgetter
list=[]
while True:
    line=input("请输入：")
    if line:
        a=tuple([x for x in line.split(",")])
        list.append(a)
    else:
        break;
print(sorted(list,key=itemgetter(1,2)))

