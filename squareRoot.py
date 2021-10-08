print('Welcome to simple calculator\n')

print('press "^" to get the square of the number')

sym=input()
num1=float(input('Enter number1 :'))
res=0
if sym=='^':
    res=num1*num1

print(res)