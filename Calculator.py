#Update to make x, ×, ÷ and : available to use, as well 'plus', 'minus'
number1 = input("Enter first number: ")
operation = input("Enter operation : ")
number2 = input("Enter second number: ")

if operation in ('+', 'plus'):
    result_plus = float(number1) + float(number2)
    print(f"{number2} + {number2} =  {result_plus}")
elif operation in ('-', 'minus'):
    result_minus = float(number1) - float(number2)
    print(f"{number1} - {number2} = {result_minus}")
elif operation in ('*', 'x', '×'):
    result_multi = float(number1) * float(number2)
    print(f"{number1} × {number2} = {result_multi}")
elif operation in ('/', '÷', ':'):
    if number2 == '0':
        print("Cannot divide by zero")
    else:
        result_division = float(number1) / float(number2)
        print(f"{number1} : {number2} = {result_division}")
