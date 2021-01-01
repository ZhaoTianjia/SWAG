# for i in range (1, 10) :
#     for j in range (i):
#         print (f'{i} * {j+1} = {i*(j+1)}', end="\t")
#         # if i==j+1:
#         #     break
#     print()
# content = ''
#
# for i in range (1, 10) :
#     for j in range (9):
#         content = content + f'{i} * {j+1} = {i*(j+1)}, '
#         # if i==j+1:
#         #     break
#     content = content + '\n'
# print(content)
# file = open('a.csv', 'w')
# file.write(content)
# print ('\a')
# str = 'swaggoose'
# print(str[0:5])
# print(str[0:9:2])
# print(str[:5])
# print(str[5:])
#
# str = "The administrative officer will report to the Director"
# print(str.split(' '))
testlist=[1,2,3,'test','list']
# for i in testlist:
#     print (i)
# print (type(testlist[2]))
# length= len(testlist)
# i=0
# while i< length:
#     print (testlist[i])
#     i=i+1
# test=input("input a testwprd  ")
# testlist.append(test)
# for i in testlist:
#     print (i)
# testlist2=[4,5]
# testlist.extend(testlist2)
# testlist.append(testlist2)
# print (testlist)
# testlist.insert(2,7)
# print(testlist)
# del testlist[2]
# print(testlist)
# print(1 == '1')
# a=[1,1,2,2,4,5,6,7,8]
# print(a. index(1,0,4))
# print (a.count(5))
# a = [[], [66,654,33], []]
# a[1].append(1)
# # a[1]=[1]
# print(a) # [[], [1], []]
office=[[],[],[]]
names=['a','b','c','d','e','f','g']
import random
for name in names:
    b=random.randint(0,2)
    office[b].append(name)
    # if b == 1:
    #     office[0].append(name)
    # if b == 2:
    #     office[1].append(name)
    # if b == 3:
    #     office[2].append(name)
print(office)

