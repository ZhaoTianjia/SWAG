def add(x, y):
    return x+y

def abs(x):
    if x>=0:
        return x
    else:
        return -x

# f(n) = 1*2*3*...*(n-1)*n
# def factorial(n):
#     result=1
#     for i in range (n):
#         result= result*(i+1)
#     return result

# f(n) = if n == 0 then 1 else (f(n - 1) * n)
def factorial(n):
    # print(f'calculating f({n})')
    if n == 0:
        # print(f'f({n}) result is 1')
        return 1
    result = (factorial(n-1)) * n
    # print(f'f({n}) result is {result}')
    return result

# f(n) = f(n - 1) + f(n - 2)
#        if n == 0: 0
#        if n == 1: 1
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        result= fibonacci(n - 1) + fibonacci(n - 2)
        return result



def sum(list):
    result=0
    for i in list:

        result=result+ i
    return result

import math
def max(list):
    result=-math.inf
    for item in list:
        if result> item:
            continue
        else:
            result=item
    return result

def median(list):
    list.sort()
    if len(list)%2==0:
        num1=len(list)//2
        num2=len(list)//2-1
        return(list[num1]+list[num2])/2
    else:
        num= (len(list)-1)//2
        return list[num]

assert add(0, 0) == 0
assert add(0, 1) == 1
assert add(1, 1) == 2
assert add(4, 5) == 9
print("✌️ 'add' is correct!")
assert abs(4) == 4
assert abs(-4) == 4
assert abs(0) == 0
print("✌️ 'abs' is correct!")
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(7) == 5040
assert factorial(8) == 40320
assert factorial(9) == 362880
assert factorial(10) == 3628800
assert factorial(0) == 1
print("✌️ 'factorial' is correct!")
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(9) == 34
assert fibonacci(10) == 55
print("✌️ 'fibonacci' is correct!")
assert sum([]) == 0
assert sum([0]) == 0
assert sum([1]) == 1
assert sum([3,4,5,6]) == 18
assert sum([3,4,-5,6]) == 8
print("✌️ 'sum' is correct!")
assert max([0]) == 0
assert max([1]) == 1
assert max([6,7,3,4,5]) == 7
assert max([-6,-7,-3,-4,-5]) == -3
print("✌️ 'max' is correct!")
assert median([0]) == 0
assert median([0]) == 0
assert median([1]) == 1
assert median([6,7,3,4,5]) == 5
assert median([3,4,-5,6,7]) == 4
assert median([3,6,4,6]) == 5
print("✌️ 'median' is correct!")