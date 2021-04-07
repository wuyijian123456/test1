# class Demo:
# #     def generator(self,n):
# #         list=[]
# #         for i in range(n):
# #             if int(i)%7==0:
# #                 list.append(str(i))
# #         else:
# #             pass
# #         a=",".join(list)
# #         return a
# # n=int(input("请输入n的值："))
# # object1=Demo()
# # print(object1.generator(n))

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print(i)








