print ("calculator program (+,-,/,*)")
num1 =float(input("1st number: "))
operation = input("operator: ")
num2 = float(input("2nd number: "))

if operation == '+':
    print(num1 + num2)
elif operation =='-':
    print(num1 - num2)
elif operation == '/':
    print (num1 / num2)
elif operation == '*':
    print(num1 * num2)
else:
    print("invalid operator")