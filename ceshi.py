import operator

# encoding:utf-8
# operator 只能处理数字，字符串，列表。不能处理字典！
dict1 = {'Name': 'Mahnaz', 'Age': 7, 'height': '170cm'}
dict2 = {'AAA': 123, 'BBB': 345, 'Name': 'Mahnaz', "Classroom": 1, 'Age': 27}
for i in dict1:
    print("i-->", i)

list1 = list(dict1.keys())
list2 = list(dict2.keys())
print(type(list1))
print('list1', list1)
print('list2', list2)
print('====================================')
# for key in dict1:
#     if (key in dict1) and (dict1[key] == dict2[key]):
#         print("true!")
#     else:
#         print("false!")
a = []
if a:
    print(" a is NOT False/0/None/'' ")
else:
    print(" a is False/0/None/'' ")