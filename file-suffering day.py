#
#
# f=open('test.txt','r')
# content=f.read(5)
# print(content)                                             #读取文件是一开始光标在文件开头， 读取一次，光标前进一次
# f.close()
#
# f = open('test.txt','r')
# content=f.readlines()
# print (content)
# f.close()
#
# def copy_file():
#     content = None
#     with open('gocrazy4.txt','r') as in_file:
#         content = in_file.readlines()
#         with open('gocrazy2.txt', 'w') as out_file:
#             out_file.writelines(content)
#
# def getusername():
#     try:
#         blabla
#     except ...:
#         return ""
#
# try:
#     copy_file()
# except FileNotFoundError as e:
#     print(e)

# None
f =open('gocrazy.txt','r')
for i, line in enumerate(f):
    print(i, line)

# name2 = "weilian"
# name = "ergou"
#
# print(name, name2)
#
# temp = name2
# name2 = name
# name = temp
#
# print(name, name2)
#
# name, name2 = name2, name
#
#
# print(name, name2)

# a = []
# for i in range(10):
#     a.append(i * 2)
a = [i * 2 for i in range(10)]
print(a)

# height = None
# if name == "ergou":
#     height = 2.0
# else:
#     height = 1.0

height = 2.0 if name == 'ergou' else 1.0
print(height)

# content=f.readlines()
# i=1
# for temp in content:
#     print(f'{i}',temp)                                     #why temp doesnt need ''.
#     i=i+1
#
# import os                                                    # 引入os模块
# os.rename('test.txt','gocrazy.txt' )
