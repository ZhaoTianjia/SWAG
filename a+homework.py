# a = int(input('your input is '))
# assert a<=2,'oops'
# if a == 0 :
#     print (f'your input is scissors {a}')
# elif a == 1 :
#     print(f'your input is rock {a}')
# else :
#     print (f'your input is paper {a}')
#
# import random
# b = random.randint(0,2)
# print (f'the random number is {b}')
#
# if a == b:
#     print ('tie')
# elif a == b+1 or a == b-2 :
#     print ('you win')
# # else :
# #     print ('you lose')
# for i in range (5) :
#     print (i)
#
# for i in range (0, 10, 3) :
#     print (i)
# name = 'swaggoose'
# for x in name :
#     print (x, end='\t')
# a=['aa','bb','cc', 'dd']
# b=len(a)
# for i in range(b):
#     print (i)

# a=['aa','bb','cc', 'dd']
# i = 16
# while i // 2 != 1:
#     print(i)
#     # print('hello')
#     # print('world')
#     i = i // 2
#
# print('end')

# print(s)
# i=12
# while i >= 11:
#     print('sleep now')
# #     i= i-1
#
# s = input('> ')
# for i in range(len(s)) :
#     print (s[i],s[len(s)-i-1],s[i]==s[len(s)-i-1] )

# count=0
# while count<5:
#     print(count, 'smaller than 5')
#     count= count+1
# else:
#     print(count, 'equal to or more tahn 5')
i=0
while i<10:
    print ('-'*30)
    i=i+1
    if i == 5 :
        continue
    print (i)


