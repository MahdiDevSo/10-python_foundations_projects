# # 6. Simple Calculator
# Idea: Add, subtract, multiply, divide

x = int(input('first number:'))
y = int(input('second number:'))

opertion = input(' opertors (+ - * / % // **): ')


if opertion == '+':
    print( 'Result is ' , x + y)
elif opertion == '-':
    print( 'Result is ' , x - y)
elif opertion == '*':
    print( 'Result is ' , x * y)
elif opertion == '/':
    print('Result is ' , x / y)
elif opertion == '%':
    print( 'Result is ' , x % y)
elif opertion == '//':
    print('Result is ' , x // y)
elif opertion == '** ':
    print('Result is  ' , x ** y)
else:
    print("Invalid operator")

