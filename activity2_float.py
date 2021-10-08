print('Welcome to simple calculator\n')

print('press "+" to summation\npress "-" to substraction\npress "*" to multiplication\npress "/" to divide')

sym=input()
num1=float(input('Enter first number :'))
num2=float(input('Enter second number :'))
res=0
if sym=='+':
    res=num1+num2
elif sym=='-':
    res = num1-num2
elif sym=='*':
    res = num1*num2
elif sym=='/':
    res = num1/num2

print(res)
