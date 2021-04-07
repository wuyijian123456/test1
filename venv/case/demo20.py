import math
lines=[]
y=[]
x=[]
while True:
    line = input("请输入：")
    if line:
        lines.append(line)
    else:
        break;
for i in lines:
    if "UP" in i:
        y.append(eval(i[3:]))
    if "DOWN" in i:
        y.append(eval("-"+i[5:]))
    if "LEFT" in i:
        x.append(eval(i[5:]))
    if "RIGHT" in i:
        x.append(eval("-" + i[6:]))
a=math.pow(sum(x),2)
b=math.pow(sum(y),2)
print(round(math.sqrt(a+b)))

