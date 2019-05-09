num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
op = input("Enter operator to perform operation: ")
if op == '+':
    print("The sum of " + str(num1) + " and " + str(num2) + " = " +str(num1+num2))
elif op == '-':
    print("The subtraction of " + str(num1) + " and " + str(num2) + " = " +str(num1-num2))
elif op == '*':
    print("The multiplication of " + str(num1) + " and " + str(num2) + " = " +str(num1*num2))
elif op == '/':
    print("The division of " + str(num1) + " and " + str(num2) + " = " +str(num1/num2))
elif op == '%':
    print("The mod of " + str(num1) + " and " + str(num2) + " = " +str(num1%num2))
else:
    print("Invalid Input")