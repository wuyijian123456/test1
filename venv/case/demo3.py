a,b=(1,2)
print(a,b)
c=(1,2,2,2,[1,3,5,7])

print(c)
list=[]
for i in c:
    list.append(i)
print(list)
list[4].append(5)
print(list)
print(tuple(list))
# print(list[c])
# print(max(c))
list=[]
# for i in c[4]:
#     list.append(i)
# list.append(5)
print(list)
print(tuple(list))

print(type(c))
print(c.count(2))



#print(c.index([1,2,3,4]))
# for i in range(1,10):
#     print(i)

