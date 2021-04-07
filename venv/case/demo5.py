#
#
#
# # str1 = "12345"
# # list1 = list(str1)
# # print (list1)
# # b=",".join(list1)
# # print(b)
# # print(type(b))
# # c=b.split(",")
# # print(c)
# a=["1","3","5",6]
# b=",".join(map(str,a))
# c=b.replace(",","")
# print(type(b))
# d=list(c)
# print(d)
# print(d.index("1"))
# d.remove("6")
# print(d)
# d.insert(3,6)
# print(d)
# re=d  a
# print(re)

# d.pop()
# print(d)
# d.append(6)
# print(d)

# 从控制台接收逗号分隔的数字序列并生成一个列表和一个包含每个数字的元组的程序。
#
# 假设向程序提供了以下输入：
#
# 34,67,55,33,12,98
#
# 那么，输出应该是：
#
# ['34', '67', '55', '33', '12', '98']
#
# ('34', '67', '55', '33', '12', '98')
#
# values=str (input("请输入值："))
# l=values.split(",")
# t=tuple(l)
# print(l)
# print (t)

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()


# class InputOutString():
#     def __int__(self):
#         self.s=""
#     def getString(self):
#         self.s=input()
#     def printString(self):
#         print(self.s.upper())
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
#






