import json
dict={}
dict['name']='xiaoming'
dict['age']=18
dict['sex']='f'
dict['sex']='m'
print(dict)
dict2=dict.copy()
print(len(dict))
dict2['telphone']='13720011992'
print(dict,dict2)

print(dict['name'])
print('xiaoming' in dict.values())
#dict.clear()
dict.pop('name')
print(dict)
print(dict.get('name1',100))
r=json.dumps(dict)
a='123456'
for i in a[::-2]:
    print(i)
for i in range(1,10,2):
    if 2*i>10:
        print(i)
print(json.loads(a))
print(type(json.loads(a)))
print(r)
print(type(r))
m=dict.values()
print(m)
for i in m:
    print(i)
for i in dict:
    print(i,dict[i])
list=[]
for i in dict:
    list.append(dict[i])
print(list)
list.insert(3,1)
print(list)
#list.remove(1)
#c=list.__add__(2)
#print(c)
list2=list.copy()
list3=list+list2
print("list3:",list3)
print(list.count('m'))
print(list3.count('m'))

#name=input('输入姓名：')
#list.append(name)
#print(list)
#set(list)
#print(set(list))





