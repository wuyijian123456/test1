x=int(input("x:"))
y=int(input("y:"))

list_x=[]
for  a in range(x):
    list_y=[]
    for b in range(y):
        s=b*a
        list_y.append(s)
    list_x.append(list_y)
print(list_x)







