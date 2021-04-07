lines=[]
D=[]
W=[]
while True:
    line=input("请输入：")
    if line:
        lines.append(line)
    else:
        break;
for i in lines:
    if i[0] =="D":
        D.append(i[2:])
    if i[0]=="W":
        D.append("-"+i[2:])
print(sum(map(int,D)))





