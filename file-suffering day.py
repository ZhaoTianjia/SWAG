#
#
# f=open('test.txt','r')
# content=f.read(5)
# print(content)                                             #读取文件是一开始光标在文件开头， 读取一次，光标前进一次
# f.close()
#
# f =open('test.txt','r')
# content=f.readlines()
# print (content)
# f.close()

f =open('test.txt','r')
content=f.readlines()
i=1
for temp in content:
    print(f'{i}',{temp})                                     #why temp doesnt need ''.
    i=i+1

import os                                                    # 引入os模块
os.rename('test.txt','gocrazy.txt' )
