# s1=set()
# s1.add(2)
# t=(3,5)
# s1.add(t)
# s1.update(t)
# print(s1)
# import random
# dict={}
# for i in range(1,10):
#     ran=random.randint(1,9)
#     dict[ran]=dict.get(ran,0)
#     if ran in dict:
#         dict[ran]+=1
# print(dict)

import random
list=[]
for i in range(10):
    ran=random.randint(1,15)
    list.append(ran)
print(list)
print(set(list))

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
a=','.join(l)
print(','.join(l))
print(type(a))



# def f(x):
#     if x==0:
#         return 1
#     elif x<0:
#         return ('请重新输入')
#     else:
#         return x * f(x-1)
# x=int(input("请输入一个整数："))
# print(f(x))
#还有一种解法：
# a =int(input("请输入一个整数："))
# s=1
# if a==0:
#     s = 1
# else:
#     for i in  range(1,a+1):
#         s=s*i
# print(s)



# dict={}
# # a= int(input("请输入个整数："))
# # for i in range(1,a+1):
# #     dict[i]=i*i
# # # print(dict)

a= str(input("请输入个整数："))
l=a.split(",")
print (type(l))

print(l)
print(id(1))
print(tuple(l))

