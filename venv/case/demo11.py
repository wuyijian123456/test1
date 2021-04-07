# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
#
# print (','.join(value))


# 编写一个程序，它将找到1000到3000之间的所有这些数字（都包括在内），使每个数字都是偶数。
# 获得的数字应按逗号分隔的顺序打印在一行上。
#
# 提示：
#
# 如果向问题提供了输入数据，则应假定它是控制台输入。
# list=[]
# for i  in range(1000,3001,2):
#     i=str(i)
#     list.append(i)
# print(list)
# print(','.join(list))



a=input("请输入：")
str1=[]
int1=[]
num=0
num2=0
for i in a:
    if i.isalpha():
        str1.append(i)
    if i.isupper():
        num+=1
    if i.islower():
        num2+=1



    elif i.isalnum():
        int1.append(i)
    else:
        continue
print("字母",len(str1))
print("数字",len(int1))
print("小写字母"+str(num2))
print("大写字母"+str(num))





